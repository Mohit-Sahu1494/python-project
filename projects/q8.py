# Q8. Write a program using while loop to compute sum of first N natural numbers.

n = int(input("Enter N: "))
sum_n = 0
i = 1

while i <= n:
    sum_n += i
    i += 1

print(f"Sum of first {n} natural numbers is: {sum_n}")
