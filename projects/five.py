# Q.5 Write a program using nested if-else to check if a number is positive, negative or zero.


num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")