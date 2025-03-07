import os
import sys
from db_config import get_db_connection, create_students_table
from csv_importer import import_csv_to_db
from data_analyzer import display_all_records, display_summary_statistics

def main():
    print("\n" + "=" * 50)
    print("===== Student Database Analysis System =====")
    print("=" * 50)
    
    # Define the path to the CSV file
    csv_file_path = os.path.join("data", "students.csv")
    print(f"\nInitializing application...")
    print(f"Working directory: {os.getcwd()}")
    
    try:
        # Get database connection and create table if needed
        print("\n----- DATABASE SETUP -----")
        connection = get_db_connection()
        create_students_table(connection)
        print("Closing initial database connection")
        connection.close()
        
        # Import data from CSV
        print("\n----- DATA IMPORT PROCESS -----")
        print(f"Starting import from CSV file: {csv_file_path}")
        if not import_csv_to_db(csv_file_path):
            print("Failed to import data. Exiting.")
            return
        
        print("\nYou can now check MySQL Workbench to verify the student_records table has been populated")
        
        # Display records and statistics
        print("\n----- DATA ANALYSIS -----")
        display_all_records()
        display_summary_statistics()
        
        print("\n" + "=" * 50)
        print("Program completed successfully.")
        print("=" * 50)
    
    except Exception as e:
        print(f"\nERROR: {e}")
        print("Program execution failed")
        return

if __name__ == "__main__":
    main()