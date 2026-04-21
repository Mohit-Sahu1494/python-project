# Q16. Write functions to organize a program that performs basic operations on strings and lists.

def process_string(s):
    print(f"\nProcessing String: '{s}'")
    print(f"Uppercase: {s.upper()}")
    print(f"Reversed: {s[::-1]}")
    print(f"Vowel count: {sum(1 for char in s.lower() if char in 'aeiou')}")

def process_list(lst):
    print(f"\nProcessing List: {lst}")
    print(f"Sum: {sum(lst)}")
    print(f"Average: {sum(lst) / len(lst)}")
    print(f"Max: {max(lst)}")

if __name__ == "__main__":
    test_str = "OpenAI"
    process_string(test_str)

    test_list = [10, 15, 20, 25]
    process_list(test_list)
