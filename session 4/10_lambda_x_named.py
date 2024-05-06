# Sort List of Dictionaries by Multiple Keys:
#    Given a list of dictionaries, sort the list based on multiple keys in
#    each dictionary.
# List of dictionaries
data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}, {'name': 'Doe', 'age': 35}]
# Define a named function to extract the sorting key
def sort_key(item):
    return item['name'], item['age']
# Sort the list of dictionaries based on multiple keys using a lambda function
sorted_data = sorted(data, key=lambda x: sort_key(x))
# Print the sorted list
print(sorted_data)



# Filter List of Strings with Specific Length:
#    Given a list of strings, filter out the strings with a length greater than a specified value.
# List of strings
strings = ['apple', 'banana', 'orange', 'pear', 'kiwi']
# Define a named function to check the string length
def check_length(s, length):
    return len(s) <= length
# Filter the list of strings using a lambda function with a named function
filtered_strings = list(filter(lambda x: check_length(x, 5), strings))
# Print the filtered list
print(filtered_strings)



# Calculate Factorials of Numbers with Recursion:
#    Given a list of numbers, calculate the factorial of each number using recursion.
# Define a named function for factorial calculation with recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the factorial of each number using a lambda function with a named function
factorials = list(map(lambda x: factorial(x), numbers))
# Print the list of factorials
print(factorials)




# Find Maximum Value in List of Tuples with Key Function:
#    Given a list of tuples, find the tuple with the maximum value based on a specific element in each tuple.
# List of tuples
data = [('John', 30), ('Jane', 25), ('Doe', 35)]
# Define a named function to extract the maximum age
def get_age(item):
    return item[1]
# Find the tuple with the maximum age using a lambda function with a named function
max_tuple = max(data, key=lambda x: get_age(x))
# Print the tuple with the maximum age
print(max_tuple)


