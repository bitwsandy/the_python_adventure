# Exercise 4: Dictionary Merge
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}
merged_dict = {**dict1, **dict2}
for key, value in dict1.items():
    if key in dict2:
        merged_dict[key] = [value, dict2[key]]
print("Merged dictionary:", merged_dict)
