"""
Additional SQL Queries Exercise

This script provides a framework for practicing SQL queries on the student_records table.
Your task is to fill in the SQL queries to implement the following functionality:

1. Performance category classification
2. Letter grade assignment with statistics by grade
3. Gap analysis between consecutively ranked students

Usage:
    python additional_queries_exercise.py
"""

import os
import sys
from db_config import get_db_connection
from rich.console import Console
from rich.table import Table

console = Console()

def run_performance_category_query():
    """
    Query 1: Classify students into performance categories based on CGPA ranges
    and count how many students are in each category.
    
    Expected categories:
    - Excellent: CGPA >= 3.8
    - Very Good: CGPA >= 3.5
    - Good: CGPA >= 3.3
    - Satisfactory: CGPA >= 3.0
    - Needs Improvement: CGPA < 3.0
    """
    console.print("\n[bold cyan]QUERY 1: Student Performance Categories[/bold cyan]")
    console.print("Classifying students into performance categories based on CGPA...")
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # TODO: Write a SQL query that:
            # 1. Uses CASE statement to classify students into performance categories
            # 2. Groups by performance category
            # 3. Calculates COUNT, MIN, MAX, and AVG of CGPA for each category
            # 4. Orders results by min_cgpa in descending order
            sql = """
            -- Replace this comment with your SQL query
            -- Hint: Use a CASE statement to create the performance_category column
            -- Example: CASE WHEN condition THEN value ... END AS column_name
            """
            
            console.print(f"Executing query: Performance classification")
            cursor.execute(sql)
            results = cursor.fetchall()
            
            # Display results in a table
            table = Table(title="Student Performance Categories")
            table.add_column("Performance Category", style="cyan")
            table.add_column("Student Count", style="magenta")
            table.add_column("Min CGPA", justify="right")
            table.add_column("Max CGPA", justify="right")
            table.add_column("Avg CGPA", justify="right")
            
            for row in results:
                table.add_row(
                    row['performance_category'],
                    str(row['student_count']),
                    f"{row['min_cgpa']:.2f}",
                    f"{row['max_cgpa']:.2f}",
                    f"{row['avg_cgpa']:.2f}"
                )
            
            console.print(table)
    
    finally:
        connection.close()

def run_letter_grade_query():
    """
    Query 2: Assign letter grades to students and list students with their grades
    
    Letter Grade Scale:
    - A+: CGPA >= 3.9
    - A: CGPA >= 3.7
    - A-: CGPA >= 3.5
    - B+: CGPA >= 3.3
    - B: CGPA >= 3.0
    - B-: CGPA >= 2.7
    - C+: CGPA >= 2.3
    - C: CGPA >= 2.0
    - F: CGPA < 2.0
    """
    console.print("\n[bold cyan]QUERY 2: Letter Grade Assignment[/bold cyan]")
    console.print("Assigning letter grades to students based on CGPA...")
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # TODO: Write a SQL query that:
            # 1. Selects id_no, name, cgpa
            # 2. Uses CASE statement to assign letter grades based on CGPA ranges
            # 3. Orders results by CGPA in descending order
            sql = """
            -- Replace this comment with your SQL query for individual student grades
            -- Hint: Use a CASE statement to create the letter_grade column
            """
            cursor.execute(sql)
            student_results = cursor.fetchall()
            
            # TODO: Write a second SQL query that:
            # 1. Uses the same CASE statement to assign letter grades
            # 2. Groups the results by letter_grade
            # 3. Counts how many students received each grade
            # 4. Orders by CGPA (MIN) in descending order
            sql2 = """
            -- Replace this comment with your SQL query for grade distribution
            -- Make sure your CASE statement matches the one above
            """
            cursor.execute(sql2)
            grade_stats = cursor.fetchall()
            
            # Display student grades
            table1 = Table(title="Student Letter Grades")
            table1.add_column("ID", style="dim")
            table1.add_column("Name", style="cyan")
            table1.add_column("CGPA", justify="right")
            table1.add_column("Grade", style="magenta bold")
            
            for student in student_results:
                table1.add_row(
                    student['id_no'],
                    student['name'],
                    f"{student['cgpa']:.2f}",
                    student['letter_grade']
                )
            
            console.print(table1)
            
            # Display grade distribution
            table2 = Table(title="Grade Distribution")
            table2.add_column("Letter Grade", style="magenta bold")
            table2.add_column("Count", justify="right")
            table2.add_column("Percentage", justify="right")
            
            total_students = len(student_results)
            for grade in grade_stats:
                percentage = (grade['count'] / total_students) * 100
                table2.add_row(
                    grade['letter_grade'],
                    str(grade['count']),
                    f"{percentage:.1f}%"
                )
            
            console.print(table2)
    
    finally:
        connection.close()

def run_gap_analysis_query():
    """
    Query 3: Analyze the CGPA gaps between consecutively ranked students
    """
    console.print("\n[bold cyan]QUERY 3: CGPA Gap Analysis[/bold cyan]")
    console.print("Analyzing the gaps between consecutively ranked students...")
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # TODO: Write a SQL query that:
            # 1. Selects id_no, name, and cgpa from student_records
            # 2. Orders results by CGPA in descending order to get rankings
            sql = """
            -- Replace this comment with your SQL query to get students ordered by CGPA
            -- Hint: Use ORDER BY to get the ranking right
            """
            cursor.execute(sql)
            students = cursor.fetchall()
            
            # Calculate gaps manually (using Python instead of SQL for this part)
            table = Table(title="CGPA Gap Analysis")
            table.add_column("Rank", justify="right", style="dim")
            table.add_column("ID", style="dim")
            table.add_column("Name", style="cyan")
            table.add_column("CGPA", justify="right")
            table.add_column("Gap", justify="right", style="magenta")
            
            # Find largest gap for highlighting
            gaps = []
            for i in range(len(students) - 1):
                current_cgpa = students[i]['cgpa']
                next_cgpa = students[i+1]['cgpa']
                gap = current_cgpa - next_cgpa
                gaps.append(gap)
            
            max_gap = max(gaps) if gaps else 0
            
            # Populate table with gap analysis
            for i, student in enumerate(students):
                rank = i + 1
                
                # Calculate gap with next student
                if i < len(students) - 1:
                    next_student = students[i+1]
                    gap = student['cgpa'] - next_student['cgpa']
                    gap_str = f"{gap:.2f}"
                    
                    # Highlight largest gap
                    if gap == max_gap:
                        gap_str = f"[bold red]{gap_str}[/bold red]"
                else:
                    gap_str = "N/A"  # Last student has no gap
                
                table.add_row(
                    str(rank),
                    student['id_no'],
                    student['name'],
                    f"{student['cgpa']:.2f}",
                    gap_str
                )
            
            console.print(table)
            
            # Provide analysis of the largest gap
            if max_gap > 0:
                largest_gap_index = gaps.index(max_gap)
                higher_student = students[largest_gap_index]
                lower_student = students[largest_gap_index + 1]
                
                console.print("\n[bold]Gap Analysis:[/bold]")
                console.print(f"The largest CGPA gap ({max_gap:.2f}) is between:")
                console.print(f"  - {higher_student['name']} (CGPA: {higher_student['cgpa']:.2f})")
                console.print(f"  - {lower_student['name']} (CGPA: {lower_student['cgpa']:.2f})")
                
                # Calculate average gap
                avg_gap = sum(gaps) / len(gaps) if gaps else 0
                console.print(f"The average gap between consecutive students is {avg_gap:.3f}")
    
    finally:
        connection.close()

def main():
    """Execute all three query exercises"""
    console.print("[bold green]=== SQL Query Exercises ===[/bold green]")
    
    try:
        # Run all three queries
        run_performance_category_query()
        run_letter_grade_query()
        run_gap_analysis_query()
        
        console.print("\n[bold green]All queries executed successfully![/bold green]")
    
    except Exception as e:
        console.print(f"\n[bold red]ERROR: {e}[/bold red]")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())