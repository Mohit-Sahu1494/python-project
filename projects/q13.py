# Q13. Write a program to perform tuple operations and demonstrate immutability.

my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

# Accessing elements
print("Element at index 1:", my_tuple[1])

# Slicing
print("Sliced Tuple:", my_tuple[1:4])

# Concatenation
new_tuple = my_tuple + (60, 70)
print("Concatenated Tuple:", new_tuple)

# Demonstrating immutability
print("\nTrying to modify an element (my_tuple[0] = 100):")
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"Error: {e}")
    print("This shows tuples are immutable.")
