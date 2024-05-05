# Exercise 1: Unique Elements
original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 9, 5]
unique_elements = []
for element in original_list:
    if element not in unique_elements:
        unique_elements.append(element)
print("Unique elements:", unique_elements)