import os
import csv
import time
from db_config import get_db_connection
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.table import Table

# Create a console instance for rich output
console = Console()

def import_csv_to_db(csv_file_path):
    """
    Import data from a CSV file into the student_records table.
    """
    # Check if file exists
    if not os.path.exists(csv_file_path):
        console.print(f"[bold red]Error:[/bold red] CSV file not found at [yellow]{csv_file_path}[/yellow]")
        return False
    
    console.print(f"Opening CSV file: [cyan]{csv_file_path}[/cyan]")
    
    connection = get_db_connection()
    try:
        # First, clear the existing table
        with connection.cursor() as cursor:
            with console.status("[bold cyan]Clearing existing data from table...[/bold cyan]") as status:
                cursor.execute("TRUNCATE TABLE student_records")
                time.sleep(0.5)  # Small delay to show the status
                console.print("[green]✓[/green] Table cleared successfully")
        
        # Now import the CSV data
        console.print("[bold cyan]Reading data from CSV file...[/bold cyan]")
        
        # Create a preview of the CSV data
        csv_preview = []
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            console.print(f"CSV header: [magenta]{', '.join(header)}[/magenta]")
            
            # Get a few rows for preview
            for i, row in enumerate(csv_reader):
                if i < 3:  # Just show first 3 rows
                    csv_preview.append(row)
                else:
                    break
        
        # Show csv preview in a table
        preview_table = Table(title="CSV Data Preview", border_style="cyan")
        for i, column in enumerate(header):
            preview_table.add_column(column)
        
        for row in csv_preview:
            preview_table.add_row(*row)
        
        console.print(preview_table)
        
        # Now actually process the file
        record_count = 0
        skipped_count = 0
        
        console.print("[bold cyan]Starting data import to MySQL...[/bold cyan]")
        
        # Read the file again for the actual import
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header
            
            # Get total rows for progress bar
            total_rows = sum(1 for row in csv.reader(open(csv_file_path))) - 1
            csv_file.seek(0)
            next(csv_reader)  # Skip header again
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[bold cyan]{task.description}[/bold cyan]"),
                BarColumn(),
                TextColumn("[bold green]{task.completed}/{task.total}[/bold green]"),
                TimeElapsedColumn(),
            ) as progress:
                import_task = progress.add_task("[cyan]Importing records...", total=total_rows)
                
                with connection.cursor() as cursor:
                    for row in csv_reader:
                        # Validate row data
                        if len(row) != 3:
                            progress.console.print(f"[yellow]Warning:[/yellow] Skipping invalid row: {row}")
                            skipped_count += 1
                            progress.update(import_task, advance=1)
                            continue
                        
                        id_no, name, cgpa = row
                        # Validate CGPA is a number
                        try:
                            cgpa = float(cgpa)
                        except ValueError:
                            progress.console.print(f"[yellow]Warning:[/yellow] Skipping row with invalid CGPA: {row}")
                            skipped_count += 1
                            progress.update(import_task, advance=1)
                            continue
                        
                        # Insert into database
                        sql = "INSERT INTO student_records (id_no, name, cgpa) VALUES (%s, %s, %s)"
                        cursor.execute(sql, (id_no, name, cgpa))
                        record_count += 1
                        progress.update(import_task, advance=1)
        
        # Commit changes
        console.print("[cyan]Committing changes to database...[/cyan]")
        connection.commit()
        
        # Create a summary panel
        summary = Panel(
            f"""[green]✓[/green] Successfully imported [bold green]{record_count}[/bold green] records from {csv_file_path}
{f"[yellow]⚠[/yellow] Skipped [bold yellow]{skipped_count}[/bold yellow] invalid records" if skipped_count > 0 else ""}
[cyan]→[/cyan] You can now check MySQL Workbench to verify the data has been populated""",
            title="Import Summary",
            border_style="green"
        )
        console.print(summary)
        return True
    
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Failed to import CSV data: {e}")
        return False
    
    finally:
        console.print("[dim]Closing database connection[/dim]")
        connection.close()