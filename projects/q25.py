# Q25. Write a program demonstrating multiple exceptions handling.

try:
    # We will simulate multiple possible exceptions
    data = [10, 20, "hello", 40]
    
    index = int(input("Enter an index to retrieve (0-3): "))
    value = data[index]
    
    # Try doing some math operation on the value
    result = value / 2
    print(f"Result is {result}")
    
except ValueError:
    print("Error: Please enter a valid integer for the index.")
except IndexError:
    print("Error: The index is out of bounds for the list.")
except TypeError:
    print("Error: Math operation failed due to incompatible types (e.g., trying to divide a string).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
