original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_keep = ['a', 'c', 'e']
filtered_dict = {key: value for key, value in original_dict.items() if key in keys_to_keep}
print("Filtered dictionary:", filtered_dict)

