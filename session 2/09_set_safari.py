# Mission: Set Safari: Exploring the Wild World of Sets

# Creating a set
my_set = {1, 2, 3, 4, 5}


# Adding elements to the set
my_set.add(6)
print("Set after adding element:", my_set)

# Removing elements from the set
my_set.remove(3)
print("Set after removing element:", my_set)

# Checking membership
print("Is 4 in the set?", 4 in my_set)

# Length of the set
print("Length of the set:", len(my_set))

# Creating another set for operations
another_set = {4, 5, 6, 7}

# Union of sets
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# Difference of sets
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# Checking if a set is a subset
print("Is {4, 5} a subset of the set?", {4, 5}.issubset(my_set))
