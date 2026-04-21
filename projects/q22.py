# Q22. Write a program to perform INSERT, UPDATE, DELETE, and SELECT operations on a database.
import sqlite3

db_name = "example2.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Setup table
cursor.execute('CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, item TEXT, qty INTEGER)')
cursor.execute('DELETE FROM inventory') # Clear previous runs

# INSERT
cursor.executemany("INSERT INTO inventory (item, qty) VALUES (?, ?)", 
                   [("Apples", 50), ("Bananas", 100), ("Oranges", 75)])
print("Inserted records.")

# SELECT
print("\nCurrent Inventory (SELECT):")
cursor.execute("SELECT * FROM inventory")
for row in cursor.fetchall():
    print(row)

# UPDATE
cursor.execute("UPDATE inventory SET qty = 120 WHERE item = 'Bananas'")
print("\nUpdated Bananas qty to 120.")

# DELETE
cursor.execute("DELETE FROM inventory WHERE item = 'Oranges'")
print("Deleted Oranges.")

# SELECT after modifications
print("\nFinal Inventory:")
cursor.execute("SELECT * FROM inventory")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
