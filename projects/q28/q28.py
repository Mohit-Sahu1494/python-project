# Q28. Write a program using pandas to read a CSV file and perform basic analysis.
import pandas as pd

file_path = "data.csv"

# Read the CSV
print("--- Reading CSV File ---")
try:
    df = pd.read_csv(file_path)
    print("First 3 rows:\n", df.head(3))
    
    print("\n--- Basic Analysis ---")
    print("\nDataset Info:")
    print(df.info())
    
    print("\nSummary Statistics for Numeric Columns:")
    print(df.describe())
    
    print("\nAverage Salary by Department:")
    dept_salary = df.groupby('Department')['Salary'].mean()
    print(dept_salary)
    
except FileNotFoundError:
    print(f"Error: Could not find {file_path}")
