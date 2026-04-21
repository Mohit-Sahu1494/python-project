# Q19. Write a program to copy contents of one file to another.

source_file = "source.txt"
dest_file = "destination.txt"

try:
    with open(source_file, "r") as src, open(dest_file, "w") as dst:
        content = src.read()
        dst.write(content)
    print(f"Successfully copied contents from {source_file} to {dest_file}.")
    
    print("\nContents of destination file:")
    with open(dest_file, "r") as check_dst:
        print(check_dst.read())

except FileNotFoundError:
    print(f"Error: {source_file} does not exist.")
