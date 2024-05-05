# Exercise 4: Dictionary Merge
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}
merged_dict = {**dict1, **dict2}
for key, value in dict1.items():
    if key in dict2:
        merged_dict[key] = [value, dict2[key]]
print("Merged dictionary:", merged_dict)


# This Python code merges two dictionaries into a single dictionary
# while handling overlapping keys by combining their values. Here's a breakdown:
#
# `dict1 = {'a': 1, 'b': 2, 'c': 3)`:
#       Defines the first dictionary `dict1`.
#
# `dict2 = {'b': 4, 'd': 5, 'e': 6)`:
#       Defines the second dictionary `dict2`.
#
# `merged_dict = {**dict1, **dict2)`:
#       Merges `dict1` and `dict2` using dictionary unpacking (`**`).
#       This creates a new dictionary `merged_dict` containing all key-value pairs
#       from both dictionaries.
#       - If there are duplicate keys, the value from `dict2` overwrites the value from `dict1`.
#
# `for key, value in dict1.items()`:
#       Iterates over each key-value pair in `dict1`.
#
# `if key in dict2:`:
#       Checks if the current key from `dict1` is also present in `dict2`.
#       - If the key is present in both dictionaries, it means there's a key overlap.
#
# `merged_dict[key] = [value, dict2[key]]`:
#       Updates the value corresponding to the overlapping key in `merged_dict`.
#       It creates a list containing the value from `dict1` and the value from `dict2`
#       for the overlapping key.
