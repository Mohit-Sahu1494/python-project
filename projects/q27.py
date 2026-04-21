# Q27. Write a program using numpy to perform array operations (creation, indexing, arithmetic).
import numpy as np

# 1. Array Creation
print("--- Array Creation ---")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)
print("Array 1:", arr1)
print("Array 2 (arange):", arr2)

# 2. Indexing and Slicing
print("\n--- Indexing ---")
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Matrix:\n", matrix)
print("Element at row 1, col 2:", matrix[1, 2])
print("First row:", matrix[0, :])
print("First column:", matrix[:, 0])

# 3. Arithmetic Operations
print("\n--- Arithmetic ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a + b =", a + b)
print("a * b =", a * b)
print("a * 3 =", a * 3)
