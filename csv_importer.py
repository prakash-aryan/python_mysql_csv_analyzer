import os
import csv
import pymysql
from db_config import get_db_connection

def import_csv_to_db(csv_file_path):
    """
    Import data from a CSV file into the student_records table.
    """
    # Check if file exists
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file not found at {csv_file_path}")
        return False
    
    print(f"Opening CSV file: {csv_file_path}")
    
    connection = get_db_connection()
    try:
        # First, clear the existing table
        with connection.cursor() as cursor:
            print("Clearing existing data from table...")
            cursor.execute("TRUNCATE TABLE student_records")
            print("Table cleared successfully")
        
        # Now import the CSV data
        print("Reading data from CSV file...")
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip header row
            header = next(csv_reader, None)
            print(f"CSV header: {', '.join(header)}")
            
            record_count = 0
            skipped_count = 0
            
            print("Starting data import to MySQL...")
            with connection.cursor() as cursor:
                for row in csv_reader:
                    # Validate row data
                    if len(row) != 3:
                        print(f"Warning: Skipping invalid row: {row}")
                        skipped_count += 1
                        continue
                    
                    id_no, name, cgpa = row
                    # Validate CGPA is a number
                    try:
                        cgpa = float(cgpa)
                    except ValueError:
                        print(f"Warning: Skipping row with invalid CGPA: {row}")
                        skipped_count += 1
                        continue
                    
                    # Insert into database
                    sql = "INSERT INTO student_records (id_no, name, cgpa) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (id_no, name, cgpa))
                    record_count += 1
        
        # Commit changes
        print("Committing changes to database...")
        connection.commit()
        print(f"Successfully imported {record_count} records from {csv_file_path}")
        if skipped_count > 0:
            print(f"Skipped {skipped_count} invalid records")
        print("You can now check MySQL Workbench to verify the data has been populated")
        return True
    
    except Exception as e:
        print(f"Error: Failed to import CSV data: {e}")
        return False
    
    finally:
        print("Closing database connection")
        connection.close()