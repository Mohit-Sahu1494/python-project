# Q6. Write a program using for loop to print multiplication table of a number.

number = int(input("Enter a number: "))
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
