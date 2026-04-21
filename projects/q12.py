# Q12. Write a program to demonstrate list slicing and list manipulation.

my_list = [1, 2, 3, 4, 5, 6, 7]
print("Original List:", my_list)

# Slicing
print("First three elements:", my_list[:3])
print("Last three elements:", my_list[-3:])
print("Every second element:", my_list[::2])

# Manipulation
my_list.append(8)
print("After appending 8:", my_list)

my_list.insert(2, 99)
print("After inserting 99 at index 2:", my_list)

my_list.remove(4)
print("After removing 4:", my_list)

popped_elem = my_list.pop()
print("After popping last element:", my_list, "| Popped:", popped_elem)
