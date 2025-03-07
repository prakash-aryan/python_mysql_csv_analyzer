import os
import sys
from db_config import get_db_connection, create_students_table
from csv_importer import import_csv_to_db
from data_analyzer import display_all_records, display_summary_statistics
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

# Create a console instance for rich output
console = Console()

def main():
    # Create a title with styling
    title = Text("Student Database Analysis System", style="bold magenta")
    
    console.print(Rule(title, style="cyan", align="center"))
    
    # Define the path to the CSV file
    csv_file_path = os.path.join("data", "students.csv")
    console.print(f"[cyan]Initializing application...[/cyan]")
    console.print(f"Working directory: [yellow]{os.getcwd()}[/yellow]")
    
    try:
        # Get database connection and create table if needed
        console.print(Panel("[bold cyan]DATABASE SETUP[/bold cyan]", 
                           border_style="cyan"))
        connection = get_db_connection()
        create_students_table(connection)
        console.print("[dim]Closing initial database connection[/dim]")
        connection.close()
        
        # Import data from CSV
        console.print(Panel("[bold cyan]DATA IMPORT PROCESS[/bold cyan]", 
                           border_style="cyan"))
        console.print(f"Starting import from CSV file: [yellow]{csv_file_path}[/yellow]")
        if not import_csv_to_db(csv_file_path):
            console.print("[bold red]Failed to import data. Exiting.[/bold red]")
            return
        
        console.print(Panel("[green]You can now check MySQL Workbench to verify the student_records table has been populated[/green]"))
        
        # Display records and statistics
        console.print(Panel("[bold cyan]DATA ANALYSIS[/bold cyan]", 
                           border_style="cyan"))
        display_all_records()
        display_summary_statistics()
        
        console.print(Rule(style="cyan"))
        console.print("[bold green]Program completed successfully.[/bold green]")
        console.print(Rule(style="cyan"))
    
    except Exception as e:
        console.print(f"\n[bold red]ERROR: {e}[/bold red]")
        console.print("[red]Program execution failed[/red]")
        return

if __name__ == "__main__":
    main()