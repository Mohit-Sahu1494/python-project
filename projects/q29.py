# Q29. Write a program using pandas to filter and group data.
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance'],
    'Salary': [50000, 70000, 65000, 52000, 80000, 75000],
    'Years_of_Experience': [3, 5, 4, 3, 7, 6]
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)

# Filtering Data: Employees with Salary > 60000
print("\n--- Filtered Data (Salary > 60000) ---")
filtered_df = df[df['Salary'] > 60000]
print(filtered_df)

# Grouping Data: Average Salary and Max Experience by Department
print("\n--- Grouped Data by Department ---")
grouped_df = df.groupby('Department').agg(
    Avg_Salary=('Salary', 'mean'),
    Max_Experience=('Years_of_Experience', 'max')
)
print(grouped_df)
