# Q7. Write a program to iterate through string, list, and dictionary using loops.

# Iterating through a string
print("Iterating through a string:")
my_string = "Python"
for char in my_string:
    print(char, end=" ")
print("\n")

# Iterating through a list
print("Iterating through a list:")
my_list = [10, 20, 30, 40]
for item in my_list:
    print(item, end=" ")
print("\n")

# Iterating through a dictionary
print("Iterating through a dictionary:")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in my_dict.items():
    print(f"{key}: {value}")
