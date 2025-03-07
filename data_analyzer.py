from db_config import get_db_connection

def display_all_records():
    """
    Display all records from the student_records table.
    """
    print("\nFetching all student records from database...")
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Select all records
            sql = "SELECT * FROM student_records ORDER BY id_no"
            print("Executing SQL query: " + sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            print(f"Query completed. Retrieved {len(results)} records")
            
            if not results:
                print("No records found in the database.")
                return
            
            # Display header
            print("\n===== ALL STUDENT RECORDS =====")
            print(f"{'ID NO':<10} {'NAME':<30} {'CGPA':<10}")
            print("-" * 50)
            
            # Display each record
            for row in results:
                print(f"{row['id_no']:<10} {row['name']:<30} {row['cgpa']:<10.2f}")
            
            print("-" * 50)
            print(f"Total Records: {len(results)}")
    
    finally:
        print("Closing database connection")
        connection.close()

def display_summary_statistics():
    """
    Display summary statistics (count, min, max, avg) for the student_records table.
    """
    print("\nCalculating summary statistics...")
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
            print("Executing statistics query...")
            cursor.execute(sql)
            stats = cursor.fetchone()
            print("Statistics calculation completed")
            
            if not stats or stats['count'] == 0:
                print("No records available for statistics.")
                return
            
            # Display statistics
            print("\n===== SUMMARY STATISTICS =====")
            print(f"Total Students: {stats['count']}")
            print(f"Minimum CGPA: {stats['min_cgpa']:.2f}")
            print(f"Maximum CGPA: {stats['max_cgpa']:.2f}")
            print(f"Average CGPA: {stats['avg_cgpa']:.2f}")
            print("=============================\n")
            
            # Find top 3 students
            print("Finding top performing students...")
            sql = "SELECT * FROM student_records ORDER BY cgpa DESC LIMIT 3"
            cursor.execute(sql)
            top_students = cursor.fetchall()
            
            if top_students:
                print("===== TOP 3 STUDENTS =====")
                print(f"{'ID NO':<10} {'NAME':<30} {'CGPA':<10}")
                print("-" * 50)
                
                for student in top_students:
                    print(f"{student['id_no']:<10} {student['name']:<30} {student['cgpa']:<10.2f}")
                print("===========================\n")
    
    finally:
        print("Closing database connection")
        connection.close()