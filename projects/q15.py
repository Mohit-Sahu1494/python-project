# Q15. Write a program using built-in functions on list, string, and dictionary.

# List built-in functions
nums = [5, 2, 9, 1, 5, 6]
print("List:", nums)
print("Length of list:", len(nums))
print("Max in list:", max(nums))
print("Min in list:", min(nums))
print("Sum of list:", sum(nums))
print("Sorted list:", sorted(nums))

# String built-in functions
text = "  python programming  "
print("\nString:", repr(text))
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Stripped:", repr(text.strip()))
print("Replaced:", text.replace("python", "java"))

# Dictionary built-in functions
data = {"a": 1, "b": 2, "c": 3}
print("\nDictionary:", data)
print("Length:", len(data))
print("Keys:", list(data.keys()))
print("Values:", list(data.values()))
