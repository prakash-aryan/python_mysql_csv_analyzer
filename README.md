# Python MySQL CSV Analyzer

## Introduction

This project demonstrates the integration of Python with MySQL databases for data analysis workflows. The system illustrates the complete process of importing data from CSV files into a relational database, creating appropriate table structures, and performing increasingly sophisticated SQL queries to derive meaningful insights.

Designed as both a learning tool and a practical reference implementation, this project showcases real-world data processing techniques that are commonly used in data analysis, business intelligence, and academic research settings.

## Purpose and Educational Value

This project serves multiple educational purposes:

1. **Database Integration**: Demonstrates how Python can interact with MySQL databases using the PyMySQL library
2. **Data Processing Pipeline**: Shows a complete ETL (Extract, Transform, Load) workflow from raw CSV data to structured database storage
3. **SQL Query Development**: Provides incrementally challenging SQL exercises from basic CRUD operations to complex analytical queries
4. **Data Visualization**: Illustrates how to present query results in a readable, formatted manner in the terminal environment
5. **Real-world Application**: Models a simplified version of academic record management and analysis

By working through this project, you'll gain practical experience with:
- Establishing secure database connections with credential management
- Parsing and validating CSV data
- Creating robust database queries
- Implementing data categorization and grading systems
- Analyzing relative performance using gap analysis
- Formatting and presenting data analysis results

## System Architecture and Components

The project follows a modular architecture with clear separation of concerns, making it easier to understand each component's responsibility and how they interact together to form a complete system.

### Core Components:

- **db_config.py**: 
  - Manages database connection configuration and security
  - Loads credentials from environment variables for better security practices
  - Implements a connection factory pattern with error handling
  - Creates the necessary database table structure with appropriate constraints
  - Provides a clean connection closure mechanism

- **csv_importer.py**: 
  - Handles the extraction and transformation of data from CSV sources
  - Implements robust CSV parsing with validation checks
  - Performs data cleaning and type conversion
  - Executes optimized SQL INSERT operations for database loading
  - Includes detailed logging of the import process

- **data_analyzer.py**: 
  - Contains the core analytical functions for student performance analysis
  - Implements database retrieval functions with optimized queries
  - Formats and displays data in human-readable tables
  - Calculates summary statistics for student performance metrics
  - Identifies top performers for recognition

- **main.py**: 
  - Orchestrates the entire data processing workflow
  - Manages the execution sequence of the application
  - Provides user feedback throughout the process
  - Handles exception management and error reporting
  - Serves as the entry point for the application

### Exercise Components:

- **additional_queries_exercise.py**: 
  - Contains structured SQL query exercises of increasing complexity
  - Provides clear instructions and expected outcomes for each exercise
  - Includes placeholder comments guiding implementation
  - Features built-in visualization of query results
  - Offers a practical platform for SQL skill development

### Data Assets:

- **data/students.csv**: 
  - Contains structured student record data featuring Star Wars character names
  - Includes student identification, names, and CGPA values
  - Serves as the raw data source for the database import process
  - Provides a balanced distribution of grade values for meaningful analysis

## Environment Setup and Configuration

### Prerequisites
Before running this project, you need:
- Python 3.10 or higher
- MySQL Server 8.0 or higher
- Access to create databases and tables on your MySQL server
- Basic understanding of SQL and Python

### Installation Process

1. **Clone or download the repository**:
   ```bash

      ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   This will install:
   - pymysql: For MySQL database connectivity
   - python-dotenv: For secure environment variable management
   - pandas: For data manipulation (optional, used in some advanced queries)
   - rich: For  terminal output formatting

4. **Database Configuration**:
   Create and Edit the `.env` file with your MySQL connection details:
   ```
   # MySQL Database Configuration
   DB_HOST=your_database_host    # e.g., localhost
   DB_PORT=3306                  # Default MySQL port
   DB_NAME=your_database_name    # Must exist on the server
   DB_USER=your_username         # Must have CREATE TABLE permissions
   DB_PASSWORD=your_password     # Store securely
   ```

5. **Database Preparation**:
   - Ensure your MySQL server is running
   - Create the database specified in your `.env` file:
     ```sql
     CREATE DATABASE your_database_name;
     ```
   - The application will automatically create the table structure when run

6. **Verify Setup**:
   Check that:
   - Your virtual environment is activated
   - Your MySQL server is accessible with the provided credentials
   - The specified database exists
   - The data/students.csv file is present in the correct location

## Application Execution and Workflow

The project is designed to guide you through a progressive learning experience, starting with fundamental database operations and moving towards more complex analytical queries.

### Step 1: Run the Main Application

Start by running the main application to establish your database, import the data, and perform basic analysis:

```bash
python main.py
```

**What this does:**

1. **Database Connection**: 
   - Establishes a secure connection to your MySQL server
   - Outputs connection details including host and port
   - Verifies database accessibility

2. **Table Creation**:
   - Checks if the `student_records` table exists
   - Creates the table with appropriate column types and constraints if needed
   - Confirms table structure is ready for data import

3. **Data Import Process**:
   - Opens and validates the CSV file structure
   - Parses the header row and confirms expected columns
   - Performs data type validation for each record
   - Handles potential errors with appropriate messaging
   - Truncates any existing data to ensure a fresh import
   - Imports each record with SQL parameterization for security
   - Provides a count of successfully imported records

4. **Data Analysis and Display**:
   - Retrieves all records with formatted SQL query
   - Presents data in a well-structured table format
   - Calculates key statistical measures (min, max, average CGPA)
   - Identifies and highlights top-performing students
   - Summarizes the overall class performance

**Expected Output:**
You will see a detailed, step-by-step progress output with formatted tables showing:
- Connection and initialization status
- Import progress and confirmation
- Complete student records in tabular form
- Statistical analysis of the CGPA distribution
- Identification of top performers

This comprehensive output allows you to verify the entire data pipeline is functioning correctly before proceeding to the exercises.

### Step 2: Complete the SQL Query Exercises

Once you've run the main application and verified that the data pipeline is functioning correctly, you can proceed to the SQL query exercises, which represent the core educational component of this project:

```bash
python additional_queries_exercise.py
```

The exercise file contains three progressively challenging query tasks, each designed to develop specific SQL skills and analytical thinking. Currently, these contain placeholder comments that you'll need to replace with working SQL statements.

#### Exercise 1: Performance Category Classification

**Learning Objectives:**
- Implementing SQL CASE statements for data categorization
- Grouping and aggregating data with GROUP BY
- Applying multiple aggregate functions in a single query
- Sorting grouped results meaningfully

**Task Description:**
Write a query that:
1. Creates a performance category label using CGPA thresholds:
   - Excellent: CGPA ≥ 3.8
   - Very Good: CGPA ≥ 3.5
   - Good: CGPA ≥ 3.3
   - Satisfactory: CGPA ≥ 3.0
   - Needs Improvement: CGPA < 3.0
2. Groups students by these categories
3. Calculates for each category:
   - Student count
   - Minimum CGPA
   - Maximum CGPA
   - Average CGPA
4. Orders results by minimum CGPA in descending order

**Visualization:**
The results will be displayed in a formatted table showing the distribution of students across performance categories with associated statistics.

#### Exercise 2: Letter Grade Assignment

**Learning Objectives:**
- Creating complex CASE expressions with multiple conditions
- Implementing academic grading standards in SQL
- Constructing multiple related queries that share logic
- Calculating percentage distributions

**Task Description:**
This exercise requires two related queries:

**Query 1:**
1. Select student ID, name, and CGPA
2. Create a letter grade column using this grading scale:
   - A+: CGPA ≥ 3.9
   - A: CGPA ≥ 3.7
   - A-: CGPA ≥ 3.5
   - B+: CGPA ≥ 3.3
   - B: CGPA ≥ 3.0
   - B-: CGPA ≥ 2.7
   - C+: CGPA ≥ 2.3
   - C: CGPA ≥ 2.0
   - F: CGPA < 2.0
3. Order results by CGPA in descending order

**Query 2:**
1. Use the identical CASE logic to ensure consistency
2. Count how many students received each letter grade
3. Group the results by letter grade
4. Order by minimum CGPA in descending order

**Visualization:**
Results will be displayed as two tables:
- Individual student grades showing ID, name, CGPA, and assigned letter grade
- Grade distribution summary showing counts and percentages for each grade

#### Exercise 3: CGPA Gap Analysis

**Learning Objectives:**
- Writing queries that enable sequential data analysis
- Understanding how to prepare data for gap calculations
- Implementing ranking and ordering in SQL
- Identifying significant performance thresholds

**Task Description:**
Write a query that:
1. Selects student ID, name, and CGPA
2. Orders the results precisely by CGPA in descending order
3. Provides the data needed for the Python code to calculate gaps between consecutive students

**Visualization:**
The results will be displayed as a ranked table showing:
- Student rank by CGPA
- Student ID and name
- CGPA value
- Gap to the next ranked student
- Highlighting of the largest performance gap
- Analysis of where the significant performance jumps occur

### Step-by-Step Exercise Completion Guide

To successfully complete these exercises:

1. **Understand the Requirements:**
   - Carefully read each exercise description
   - Note the specific columns needed in the result set
   - Pay attention to ordering requirements
   - Understand how the result will be used by the display code

2. **Implement the Queries:**
   - Open `additional_queries_exercise.py` in your preferred code editor
   - Locate the placeholder comments for each query
   - Write SQL statements that fulfill all requirements
   - Ensure your column names match exactly what the display code expects

3. **Test Incrementally:**
   - Implement one query at a time
   - Run the script after each implementation to test your solution
   - Debug any errors by checking column names and syntax

4. **Verify Results:**
   - Check that your output tables look correct and well-formatted
   - Verify that the data makes sense (e.g., grade assignments match CGPA values)
   - Confirm that ordering and grouping work as expected

5. **Refine Your Solutions:**
   - Look for opportunities to improve query efficiency
   - Ensure consistent CASE logic between related queries
   - Consider edge cases in your data categorization

## Technical Reference Information

### Database Schema Details

The `student_records` table is designed with a straightforward but effective schema optimized for academic record storage:

```sql
CREATE TABLE IF NOT EXISTS student_records (
    id_no VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cgpa FLOAT NOT NULL
)
```

**Schema Design Rationale:**
- `id_no` as VARCHAR(20): Allows for alphanumeric student IDs with prefix coding (e.g., S001)
- `name` as VARCHAR(100): Accommodates full names of various lengths with room for special characters
- `cgpa` as FLOAT: Stores cumulative grade point average with decimal precision
- PRIMARY KEY constraint: Ensures each student record is unique and optimizes lookup queries
- NOT NULL constraints: Maintains data integrity by preventing missing critical information

### Sample Dataset

The system uses a curated dataset featuring Star Wars character names to make the learning experience more engaging:

| ID_NO | NAME             | CGPA |
|-------|------------------|------|
| S001  | Luke Skywalker   | 3.7  |
| S002  | Princess Leia    | 3.9  |
| S003  | Han Solo         | 3.5  |
| S004  | Rey Skywalker    | 4.0  |
| S005  | Obi-Wan Kenobi   | 3.2  |
| S006  | Padmé Amidala    | 3.8  |
| S007  | Anakin Skywalker | 3.1  |
| S008  | Ahsoka Tano      | 3.6  |
| S009  | Din Djarin       | 3.3  |
| S010  | Grogu            | 3.4  |

**Dataset Characteristics:**
- 10 student records providing sufficient data for meaningful analysis
- CGPA values ranging from 3.1 to 4.0, representing a realistic distribution
- Strategic distribution of values to demonstrate interesting patterns in analysis
- Balanced representation across different performance categories
- Sequential student IDs for easy reference

This data structure provides an excellent foundation for practicing SQL queries ranging from simple selections to complex analytical grouping operations.

## SQL Query Development Guide

### Essential SQL Techniques for the Exercises

When implementing your solutions for the exercises, consider these SQL best practices and techniques:

1. **Effective CASE Statements**:
   ```sql
   CASE 
       WHEN condition1 THEN result1
       WHEN condition2 THEN result2
       ...
       ELSE default_result 
   END AS column_name
   ```
   - Use logical progression in condition order (often highest to lowest)
   - Ensure conditions don't overlap to avoid unexpected results
   - Include an ELSE clause to handle all possible values
   - Give meaningful aliases to derived columns

2. **Aggregate Functions**:
   - `COUNT(*)`: Count all rows in a group
   - `MIN(column)`: Find the minimum value
   - `MAX(column)`: Find the maximum value
   - `AVG(column)`: Calculate the average value
   - `SUM(column)`: Total the values in a column
   - Consider using `ROUND(AVG(column), 2)` for cleaner decimal display

3. **Grouping and Sorting**:
   - `GROUP BY`: Must include all non-aggregated columns in SELECT
   - `ORDER BY`: Can reference columns by position number (e.g., `ORDER BY 1 DESC`)
   - Multiple grouping: `GROUP BY column1, column2`
   - Multiple sorting: `ORDER BY column1 DESC, column2 ASC`

4. **Readability Practices**:
   - Use consistent indentation for nested statements
   - Place each major clause (SELECT, FROM, WHERE, etc.) on a new line
   - Use table aliases for complex queries (`FROM table_name AS t`)
   - Comment complex logic, particularly in CASE statements

5. **Common Pitfalls to Avoid**:
   - Forgetting to include columns in GROUP BY that appear in SELECT
   - Using ambiguous column names when they could appear in multiple tables
   - Missing edge cases in CASE statement conditions
   - Not handling NULL values appropriately
