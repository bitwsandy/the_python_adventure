# Mission: List Lore: Unveiling the Mysteries of Lists

# Creating a list with multiple data types
my_list = [1, "apple", 3.14, True, 45]

# Accessing elements
print("First element:", my_list[0])

# Slicing
print("Slice:", my_list[1:3])

# Appending
my_list.append("banana")
print("Appended:", my_list)

# Inserting
my_list.insert(2, "orange")
print("Inserted:", my_list)

# Removing
my_list.remove(3.14)
print("Removed:", my_list)

# Popping
popped_item = my_list.pop()
print("Popped item:", popped_item)
print("Remaining list:", my_list)

# Length
print("Length of list:", len(my_list))
