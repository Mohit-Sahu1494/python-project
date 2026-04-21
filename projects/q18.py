# Q18. Write a program to write and append data to a file.

file_path = "output_q18.txt"

# Writing to a file (Overwrites if exists)
with open(file_path, "w") as file:
    file.write("This is the first line.\n")
    file.write("Writing data overwrites existing files.\n")
print(f"Data written to {file_path}")

# Appending to a file
with open(file_path, "a") as file:
    file.write("This line is appended.\n")
    file.write("Appending adds to the end.\n")
print(f"Data appended to {file_path}")

# Verification
print("\nVerifying file contents:")
with open(file_path, "r") as file:
    print(file.read())
