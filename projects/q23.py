# Q23. Demonstrate transaction control (commit and rollback) in database operations.
import sqlite3

db_name = "example_tx.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL)')
cursor.execute('DELETE FROM accounts')
cursor.execute("INSERT INTO accounts (name, balance) VALUES ('Alice', 1000), ('Bob', 500)")
conn.commit()

# Successful Transaction
try:
    print("Attempting to transfer $200 from Alice to Bob...")
    cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE name = 'Alice'")
    cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE name = 'Bob'")
    conn.commit()
    print("Transaction committed successfully.")
except Exception as e:
    conn.rollback()
    print("Error occurred, transaction rolled back.", e)

# Failing Transaction
try:
    print("\nAttempting an invalid transaction...")
    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE name = 'Bob'")
    # Simulate an error
    raise ValueError("Something went wrong during transfer!")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE name = 'Alice'")
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Transaction failed and rolled back. Reason: {e}")

# Check final balances
print("\nFinal Balances:")
for row in cursor.execute("SELECT * FROM accounts"):
    print(row)

conn.close()
