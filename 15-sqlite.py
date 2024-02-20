import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id INTEGER PRIMARY KEY, name TEXT, salary REAL)''')

# Insert data into the table
cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ('John', 50000))
cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ('Alice', 60000))
cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ('Bob', 70000))

# Save changes to the database
conn.commit()

# Query the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

"""
Theory Question:
Explain the SQLite workflow and its significance in database management. 
Describe the key components of the SQLite workflow, including connecting to a database, creating tables, inserting data, querying data, and closing connections. 
Discuss the advantages and limitations of using SQLite compared to other database management systems.

Practical Question:
Design a Python program that demonstrates the SQLite workflow for managing employee records. The program should have the following functionalities:

Connect to an SQLite database.
Create a table to store employee records with columns for employee ID, name, and salary.
Insert multiple employee records into the table.
Query the table to retrieve and display all employee records.
Close the connection to the database.
"""