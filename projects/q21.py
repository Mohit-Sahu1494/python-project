# Q21. Write a program to connect to a database and create a table.
import sqlite3

db_name = "example.db"

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

print("Database connected and table 'students' created successfully.")

conn.commit()
conn.close()
