# Square of a Number:
#    Write a lambda function that takes a number as input and returns its square.

# Define a lambda function that takes 'x' as input and returns 'x' squared
square = lambda x: x**2
# Test the lambda function
print(square(5))  # Output: 25


# Addition of Two Numbers:
#    Write a lambda function that takes two numbers as input and returns their sum.
# Define a lambda function that takes 'x' and 'y' as input and returns their sum
addition = lambda x, y: x + y
# Test the lambda function
print(addition(3, 5))  # Output: 8


# Check Even Number:
#    Write a lambda function that takes a number as input and returns True if it's even,
#    otherwise False.
# Define a lambda function that takes 'x' as input and returns True if 'x' is even, else False
is_even = lambda x: x % 2 == 0
# Test the lambda function
print(is_even(6))  # Output: True
print(is_even(5))  # Output: False


# Reverse a String:
#    Write a lambda function that takes a string as input and returns the reversed
#    string.
# Define a lambda function that takes 's' as input and returns 's' reversed
reverse_string = lambda s: s[::-1]
# Test the lambda function
print(reverse_string("hello"))  # Output: "olleh"



# Sort List of Tuples by Second Element:
#    Write a lambda function to sort a list of tuples based on the second element of
#    each tuple.
# Define a list of tuples
data = [('John', 25), ('Doe', 30), ('Jane', 20)]
# Sort the list of tuples based on the second element using a lambda function
sorted_data = sorted(data, key=lambda x: x[1])
# Print the sorted list
print(sorted_data)  # Output: [('Jane', 20), ('John', 25), ('Doe', 30)]




# Sort List of Dictionaries by a Key:
#    Given a list of dictionaries, sort the list based on a specific key in each
#    dictionary.
# List of dictionaries
data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}, {'name': 'Doe', 'age': 35}]
# Sort the list of dictionaries based on the 'age' key using a lambda function
sorted_data = sorted(data, key=lambda x: x['age'])
# Print the sorted list
print(sorted_data)



# Filter List of Numbers:
#    Given a list of numbers, filter out the numbers that are divisible by 3.
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter the list of numbers to include only those divisible by 3 using a lambda function
filtered_numbers = list(filter(lambda x: x % 3 == 0, numbers))
# Print the filtered list
print(filtered_numbers)



# Calculate Factorials of Numbers:
#    Given a list of numbers, calculate the factorial of each number.
# List of numbers
numbers = [1,2 ,2, 3, 4, 5]
# Calculate the factorial of each number using a lambda function
factorials = list(map(lambda x: 1 if x == 0 else x * factorials(x - 1), numbers))
# Print the list of factorials
print(factorials)



# Find Maximum Value in List of Tuples:
#    Given a list of tuples, find the tuple with the maximum value based on a
#    specific element in each tuple.
# List of tuples
data = [('John', 30), ('Jane', 25), ('Doe', 35)]
# Find the tuple with the maximum age using a lambda function
max_tuple = max(data, key=lambda x: x[1])
# Print the tuple with the maximum age
print(max_tuple)



# Group List of Words by Length:
#    Given a list of words, group the words based on their lengths into a dictionary.
# List of words
words = ['apple', 'banana', 'orange', 'pear', 'kiwi']
# Group the words by length using a lambda function
grouped_words = {}
for word in words:
    length = len(word)
    grouped_words.setdefault(length, []).append(word)
# Print the grouped words
print(grouped_words)




