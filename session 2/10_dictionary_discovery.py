# Mission: Dictionary Discovery: Navigating the Realm of Dictionaries

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements
print("Name:", my_dict['name'])

# Modifying elements
my_dict['age'] = 35
print("Modified age:", my_dict['age'])

# Adding new key-value pairs
my_dict['gender'] = 'Male'
print("Added gender:", my_dict['gender'])

# Removing key-value pairs
removed_value = my_dict.pop('city')
print("Removed city:", removed_value)

# Checking if key exists
print("Is 'name' a key in the dictionary?", 'name' in my_dict)

# Length of the dictionary
print("Length of the dictionary:", len(my_dict))

# Getting keys and values
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())

# Creating another dictionary for operations
another_dict = {'country': 'USA', 'occupation': 'Engineer'}

# Merging dictionaries
my_dict.update(another_dict)
print("Merged dictionary:", my_dict)