# Q26. Write a program using finally and custom exceptions.

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    def __init__(self, message="Negative values are not allowed."):
        self.message = message
        super().__init__(self.message)

def check_positive(num):
    if num < 0:
        raise NegativeNumberError(f"{num} is a negative number!")
    return True

try:
    val = int(input("Enter a positive number: "))
    check_positive(val)
    print("You entered a valid positive number.")
except ValueError:
    print("Exception: That's not a number.")
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}")
finally:
    print("Execution of try-except block is complete. This 'finally' block always runs.")
