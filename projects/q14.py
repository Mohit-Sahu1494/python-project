# Q14. Write a program to perform dictionary operations (add, update, delete).

user_info = {"name": "Bob", "age": 30}
print("Original Dictionary:", user_info)

# Add
user_info["city"] = "Boston"
print("After adding city:", user_info)

# Update
user_info["age"] = 31
user_info.update({"email": "bob@example.com"})
print("After updating age and adding email:", user_info)

# Delete
del user_info["city"]
print("After deleting city:", user_info)

popped_val = user_info.pop("email")
print("After popping email:", user_info, "| Popped:", popped_val)
