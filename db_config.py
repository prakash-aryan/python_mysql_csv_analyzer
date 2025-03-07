import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    """
    Create and return a database connection using credentials from .env file.
    """
    print(f"Attempting to connect to MySQL server at {os.getenv('DB_HOST')}:{os.getenv('DB_PORT', 3306)}...")
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print(f"Successfully connected to database '{os.getenv('DB_NAME')}'")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

def create_students_table(connection):
    """
    Create the student_records table if it doesn't exist.
    """
    print("Checking if table exists or needs to be created...")
    with connection.cursor() as cursor:
        # Create table
        sql = """
        CREATE TABLE IF NOT EXISTS student_records (
            id_no VARCHAR(20) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            cgpa FLOAT NOT NULL
        )
        """
        cursor.execute(sql)
        print("Table 'student_records' is ready for use")
    connection.commit()