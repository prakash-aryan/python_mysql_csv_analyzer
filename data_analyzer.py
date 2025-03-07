from db_config import get_db_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Create a console instance for rich output
console = Console()

def display_all_records():
    """
    Display all records from the student_records table.
    """
    console.print("\n[bold cyan]Fetching all student records from database...[/bold cyan]")
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Select all records
            sql = "SELECT * FROM student_records ORDER BY id_no"
            console.print(f"Executing SQL query: [dim]{sql}[/dim]")
            cursor.execute(sql)
            results = cursor.fetchall()
            console.print(f"Query completed. Retrieved [green]{len(results)}[/green] records")
            
            if not results:
                console.print("[yellow]No records found in the database.[/yellow]")
                return
            
            # Create and populate a Rich table
            table = Table(title="ALL STUDENT RECORDS", border_style="cyan")
            table.add_column("ID NO", style="magenta")
            table.add_column("NAME", style="green")
            table.add_column("CGPA", justify="right", style="cyan")
            
            # Add rows to the table
            for row in results:
                table.add_row(
                    row['id_no'],
                    row['name'],
                    f"{row['cgpa']:.2f}"
                )
            
            # Display the table
            console.print(table)
            console.print(f"Total Records: [bold green]{len(results)}[/bold green]")
    
    finally:
        console.print("[dim]Closing database connection[/dim]")
        connection.close()

def display_summary_statistics():
    """
    Display summary statistics (count, min, max, avg) for the student_records table.
    """
    console.print("\n[bold cyan]Calculating summary statistics...[/bold cyan]")
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Get statistics
            sql = """
            SELECT 
                COUNT(*) as count,
                MIN(cgpa) as min_cgpa,
                MAX(cgpa) as max_cgpa,
                AVG(cgpa) as avg_cgpa
            FROM student_records
            """
            console.print("Executing statistics query...")
            cursor.execute(sql)
            stats = cursor.fetchone()
            console.print("Statistics calculation completed")
            
            if not stats or stats['count'] == 0:
                console.print("[yellow]No records available for statistics.[/yellow]")
                return
            
            # Create panel for statistics
            stats_panel = Panel(
                f"""[bold]Total Students:[/bold] {stats['count']}
[bold]Minimum CGPA:[/bold] {stats['min_cgpa']:.2f}
[bold]Maximum CGPA:[/bold] {stats['max_cgpa']:.2f}
[bold]Average CGPA:[/bold] {stats['avg_cgpa']:.2f}""",
                title="SUMMARY STATISTICS",
                border_style="green"
            )
            console.print(stats_panel)
            
            # Find top 3 students
            console.print("Finding top performing students...")
            sql = "SELECT * FROM student_records ORDER BY cgpa DESC LIMIT 3"
            cursor.execute(sql)
            top_students = cursor.fetchall()
            
            if top_students:
                # Create table for top students
                top_table = Table(title="TOP 3 STUDENTS", border_style="magenta")
                top_table.add_column("ID", style="dim")
                top_table.add_column("NAME", style="cyan")
                top_table.add_column("CGPA", justify="right", style="magenta bold")
                
                for student in top_students:
                    top_table.add_row(
                        student['id_no'],
                        student['name'],
                        f"{student['cgpa']:.2f}"
                    )
                
                console.print(top_table)
    
    finally:
        console.print("[dim]Closing database connection[/dim]")
        connection.close()