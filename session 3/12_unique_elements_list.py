# Exercise 1: Unique Elements
original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 9, 5]
unique_elements = []
for element in original_list:
    if element not in unique_elements:
        unique_elements.append(element)
print("Unique elements:", unique_elements)

# original_set = set(original_list)
# unique_elements = list(original_set)



#`unique_elements = []`:
#       Initializes an empty list to store unique elements.
#
#`for element in original_list:`:
#       Iterates over each element `element` in the `original_list`.
#
#`if element not in unique_elements:`:
#       Checks if the current element is not already in the `unique_elements` list.
#       - If the element is not in the list, it means it's unique,
#         so it appends it to the `unique_elements` list.