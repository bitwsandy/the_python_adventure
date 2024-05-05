# Exercise 10: Dictionary Aggregation
people = [
    {'name': 'Alice', 'age': 25, 'occupation': 'Engineer'},
    {'name': 'Bob', 'age': 30, 'occupation': 'Doctor'},
    {'name': 'Charlie', 'age': 20, 'occupation': 'Artist'},
    {'name': 'David', 'age': 35, 'occupation': 'Engineer'},
    {'name': 'Eve', 'age': 28, 'occupation': 'Artist'}
]
occupation_dict = {}
for person in people:
    occupation = person['occupation']
    name = person['name']
    if occupation not in occupation_dict:
        occupation_dict[occupation] = [name]
    else:
        occupation_dict[occupation].append(name)
print("Occupation dictionary:", occupation_dict)