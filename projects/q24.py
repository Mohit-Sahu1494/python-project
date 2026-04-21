# Q24. Write a program to handle exceptions using try-except blocks.

try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
