import os
import pymysql
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

# Create a console instance for rich output
console = Console()

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    """
    Create and return a database connection using credentials from .env file.
    """
    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT", 3306))
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    
    # Hide password in output for security
    masked_password = "•" * len(os.getenv("DB_PASSWORD", ""))
    
    console.print(f"[bold cyan]Attempting to connect to MySQL server...[/bold cyan]")
    console.print(f"[cyan]Host:[/cyan] {db_host}")
    console.print(f"[cyan]Port:[/cyan] {db_port}")
    console.print(f"[cyan]Database:[/cyan] {db_name}")
    console.print(f"[cyan]User:[/cyan] {db_user}")
    console.print(f"[cyan]Password:[/cyan] {masked_password}")
    
    try:
        connection = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=os.getenv("DB_PASSWORD"),
            database=db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        console.print(f"[bold green]✓ Successfully connected to database '{db_name}'[/bold green]")
        return connection
    except Exception as e:
        console.print(Panel(
            f"[bold red]Database Connection Error:[/bold red]\n{str(e)}",
            title="Connection Failed",
            border_style="red"
        ))
        raise

def create_students_table(connection):
    """
    Create the student_records table if it doesn't exist.
    """
    console.print("[bold cyan]Checking if table exists or needs to be created...[/bold cyan]")
    
    table_definition = """
CREATE TABLE IF NOT EXISTS student_records (
    id_no VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cgpa FLOAT NOT NULL
)"""
    
    with connection.cursor() as cursor:
        # Create table
        cursor.execute(table_definition)
        
        # Check if table was just created or already existed
        cursor.execute("SELECT COUNT(*) as count FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", 
                      (os.getenv("DB_NAME"), "student_records"))
        result = cursor.fetchone()
        
        if result['count'] == 0:
            console.print("[bold yellow]Table 'student_records' created[/bold yellow]")
        else:
            console.print("[green]Table 'student_records' already exists[/green]")
    
    connection.commit()
    
    # Show table structure
    with connection.cursor() as cursor:
        cursor.execute("DESCRIBE student_records")
        results = cursor.fetchall()
        
        console.print("[cyan]Table structure:[/cyan]")
        for column in results:
            console.print(f"  [green]{column['Field']}[/green]: {column['Type']} {column['Null']} {column['Key']}")
    
    console.print("[bold green]✓ Table 'student_records' is ready for use[/bold green]")