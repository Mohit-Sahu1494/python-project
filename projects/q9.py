# Q9. Demonstrate use of break, continue, and pass in loops.

print("Demonstrating 'break':")
for i in range(1, 10):
    if i == 5:
        print("Breaking at 5")
        break
    print(i, end=" ")
print("\n")

print("Demonstrating 'continue':")
for i in range(1, 8):
    if i == 4:
        print("Skipping 4", end=" ")
        continue
    print(i, end=" ")
print("\n")

print("Demonstrating 'pass':")
for i in range(3):
    if i == 1:
        pass # Placeholder for future code
    print(f"Index {i}")
