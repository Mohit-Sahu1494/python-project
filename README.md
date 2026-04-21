# Python Exercises Collection

This repository contains a collection of Python scripts covering various concepts ranging from basic loops and data structures to file handling, database operations, exception handling, and data analysis using Pandas, NumPy, and Matplotlib.

All files and scripts are located in the `projects` directory.

## Table of Contents

### Basic Concepts, Loops, and Data Structures
- **`q6.py`**: Multiplication table using a `for` loop.
- **`q7.py`**: Iterating through strings, lists, and dictionaries using loops.
- **`q8.py`**: Computing the sum of the first N natural numbers using a `while` loop.
- **`q9.py`**: Demonstration of `break`, `continue`, and `pass` statements within loops.
- **`q10.py`**: Basic string operations including slicing, concatenation, and reversing.
- **`q11.py`**: Counting the frequency of characters within a string.
- **`q12.py`**: List slicing and manipulation (adding, inserting, removing).
- **`q13.py`**: Tuple operations demonstrating immutability.
- **`q14.py`**: Dictionary operations (add, update, delete).
- **`q15.py`**: Exploring built-in functions for lists, strings, and dictionaries.
- **`q16.py`**: Functions organizing a program that performs operations on strings and lists.

### File Handling
- **`q17/` (`q17.py`)**: Reading files using `read()`, `readline()`, and `readlines()`.
- **`q18.py`**: Writing and appending data to a file.
- **`q19/` (`q19.py`)**: Copying data from a source file to a destination file.
- **`q20/` (`q20.py`)**: Demonstrating file pointer operations using `seek()`.

### Database Operations (SQLite)
- **`q21.py`**: Connecting to an SQLite database and creating tables.
- **`q22.py`**: Performing CRUD operations (INSERT, UPDATE, DELETE, SELECT).
- **`q23.py`**: Transaction control demonstrating `commit` and `rollback` operations.

### Exception Handling
- **`q24.py`**: Basic exception handling using `try-except` blocks.
- **`q25.py`**: Handling multiple distinct exceptions in a single program.
- **`q26.py`**: Using the `finally` block and creating user-defined custom exceptions.

### Data Analysis and Visualization
*Note: Ensure you have installed the required libraries via `pip install pandas numpy matplotlib` before running these scripts.*
- **`q27.py`**: Demonstrating basic `numpy` array creation, indexing, and arithmetic.
- **`q28/` (`q28.py`)**: Using `pandas` to read data from a CSV file and perform basic exploratory data analysis.
- **`q29.py`**: Filtering and grouping datasets using `pandas`.
- **`q30.py`**: Plotting data using `matplotlib` (Line and Bar graphs, exports to `q30_plot.png`).
- **`q31.py`**: Combining `numpy`, `pandas`, and `matplotlib` to generate data, analyze it (rolling average), and plot it (exports to `q31_analysis_plot.png`).

## How to Run

Navigate to the `projects` folder using your terminal:

```bash
cd projects
python q6.py  # Example command to run Question 6
```

For scripts that use data files and are located inside subfolders (such as `q17`, `q19`, `q20`, and `q28`), navigate into the specific folder first to ensure the relative file paths resolve correctly:

```bash
cd projects/q28
python q28.py
```
