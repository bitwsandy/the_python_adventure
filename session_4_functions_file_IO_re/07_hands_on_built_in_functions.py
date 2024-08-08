#
# 1. Word Frequency Counter:
#    Write a Python program that takes a string of text as input and prints the frequency of
# each word in the text. Utilize the following built-in functions:
#    - input() for taking input from the user
#    - str.split() for splitting the text into words
#    - str.lower() for converting words to lowercase
#    - str.strip() for removing leading and trailing whitespaces
#    - dict.get() for counting word frequencies using a dictionary
def word_frequency_counter(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word = word.strip(",.?!")  # Remove punctuation
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = input("Enter a text: ")
frequency = word_frequency_counter(text)
for word, count in frequency.items():
    print(f"{word}: {count}")





# 2. Temperature Converter:
#    Write a Python program that converts temperatures between Celsius and Fahrenheit.
#    Utilize the following built-in functions:
#    - float() for converting input to floating-point numbers
#    - round() for rounding temperature values
#    - input() for taking input from the user
def celsius_to_fahrenheit(celsius):
    return round(celsius * 9/5 + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ")

if unit.upper() == 'C':
    print(f"{temperature}°C is equal to {celsius_to_fahrenheit(temperature)}°F")
elif unit.upper() == 'F':
    print(f"{temperature}°F is equal to {fahrenheit_to_celsius(temperature)}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")




# 3. Palindrome Checker:
#    Write a Python function that checks if a given string is a palindrome. Utilize the following built-in functions:
#    - str.lower() for converting the string to lowercase
#    - str.replace() for removing whitespace or punctuation
#    - str[::-1] for reversing the string
#    - str.strip() for removing leading and trailing whitespaces
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")




# 4. List Manipulation:
#    Write a Python program that performs various operations on a list of numbers, such as finding the sum, average,
# maximum, and minimum. Utilize the following built-in functions:
#    - list() for creating a list
#    - sum() for finding the sum of elements in a list
#    - len() for finding the length of a list
#    - max() and min() for finding the maximum and minimum values in a list
numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]

total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")




# 5. File Word Counter:
#    Write a Python program that reads a text file and counts the frequency of each word in the file.
# Utilize the following built-in functions:
#    - open() for opening a file
#    - file.read() for reading the contents of the file
#    - str.split() for splitting the text into words
#    - str.strip() for removing leading and trailing whitespaces
#    - dict.get() for counting word frequencies using a dictionary
def word_frequency_counter(file_name):
    word_count = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word = word.strip(",.?!")  # Remove punctuation
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

file_name = input("Enter file name: ")
frequency = word_frequency_counter(file_name)
for word, count in frequency.items():
    print(f"{word}: {count}")
