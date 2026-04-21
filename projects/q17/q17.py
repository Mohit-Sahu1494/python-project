# Q17. Write a program to read contents of a file using read(), readline(), and readlines().

file_path = "sample.txt"

print("--- Using read() ---")
with open(file_path, "r") as file:
    content = file.read()
    print(content)

print("--- Using readline() ---")
with open(file_path, "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("First line:", line1.strip())
    print("Second line:", line2.strip())

print("\n--- Using readlines() ---")
with open(file_path, "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        print(f"Index {i}: {line.strip()}")
