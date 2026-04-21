# Q20. Write a program to demonstrate file pointer operations using seek().

file_path = "data.txt"

with open(file_path, "r") as file:
    print("Initial position pointer:", file.tell())
    
    # Read first 10 characters
    print("Read first 10 chars:", file.read(10))
    print("Current position pointer:", file.tell())
    
    # Seek to position 11
    file.seek(11)
    print("\nSeek to position 11.")
    print("Current position pointer:", file.tell())
    print("Read rest of file:", file.read())
    
    # Reset to beginning
    file.seek(0)
    print("\nReset pointer to start.")
    print("First 5 chars:", file.read(5))
