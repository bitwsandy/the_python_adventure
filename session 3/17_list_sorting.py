# 1. Sort a list of numbers in ascending order:



#### Perform exercises in list_sorting.py
# Given list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Sort the list in ascending order using sorted() function
sorted_numbers = sorted(numbers)

# Print the sorted list
print("Sorted numbers in ascending order:", sorted_numbers)



# 2. Sort a list of strings in alphabetical order:

# Given list of strings
strings = ['apple', 'banana', 'orange', 'kiwi', 'mango']

# Sort the list in alphabetical order using sorted() function
sorted_strings = sorted(strings)

# Print the sorted list
print("Sorted strings in alphabetical order:", sorted_strings)




# 3. Sort a list of tuples based on a specific element:

# Given list of tuples
tuples = [(3, 'apple'), (1, 'banana'), (2, 'orange'), (5, 'kiwi'), (4, 'mango')]

# Sort the list of tuples based on the first element of each tuple
sorted_tuples = sorted(tuples, key=lambda x: x[0])

# Print the sorted list of tuples
print("Sorted tuples based on the first element:", sorted_tuples)



# 4. Sort a list of dictionaries based on a specific key:

# Given list of dictionaries
dictionaries = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]

# Sort the list of dictionaries based on the 'name' key
sorted_dictionaries = sorted(dictionaries, key=lambda x: x['name'])

# Print the sorted list of dictionaries
print("Sorted dictionaries based on the 'name' key:", sorted_dictionaries)




# 5. Sort a list of tuples based on a specific element in descending order:
list_of_tuples = [('Alice', 25), ('Bob', 30), ('Charlie', 20), ('David', 35)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
print("Sorted list:", sorted_list)