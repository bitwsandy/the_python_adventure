# Dictionary Aggregation
# Given list of dictionaries representing people and their attributes
people = [
    {'name': 'Alice', 'age': 25, 'occupation': 'Engineer'},
    {'name': 'Bob', 'age': 30, 'occupation': 'Doctor'},
    {'name': 'Charlie', 'age': 20, 'occupation': 'Artist'},
    {'name': 'David', 'age': 35, 'occupation': 'Engineer'},
    {'name': 'Eve', 'age': 28, 'occupation': 'Artist'}
]

# Initialize an empty dictionary to store occupation as keys and list of names as values
occupation_dict = {}

# Iterate over each person in the list of people
for person in people:
    # Extract occupation and name from the current person dictionary
    occupation = person['occupation']
    name = person['name']

    # Check if the occupation is already in the occupation dictionary
    if occupation not in occupation_dict:
        # If not, create a new key-value pair with occupation as key and a list containing the name as value
        occupation_dict[occupation] = [name]
    else:
        # If occupation already exists in the dictionary, append the name to the existing list
        occupation_dict[occupation].append(name)

# Print the occupation dictionary
print("Occupation dictionary:", occupation_dict)
