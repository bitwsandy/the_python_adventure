# Mission: Tuple Trek: Exploring the World of Tuples

# Creating a tuple with multiple data types
my_tuple = (1, "apple", 3.14, True, 45)

# Accessing elements
print("First element:", my_tuple[0])

# Slicing
print("Slice:", my_tuple[1:3])

# Length
print("Length of tuple:", len(my_tuple))

# Concatenating tuples
another_tuple = ("banana", False)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Repetition
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# Unpacking
a, b, c, d, e = my_tuple
print("Unpacked elements:", a, b, c, d, e)
