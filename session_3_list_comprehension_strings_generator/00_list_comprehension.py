# Exercise 1: Squares of Numbers
squares = [x**2 for x in range(1, 11)]
print("Squares of numbers from 1 to 10:", squares)

# `squares = [x**2 for x in range(1, 11)]`:
#       This is a list comprehension.
#       It's a concise way to create lists in Python.
#       In this comprehension:
#       - `for x in range(1, 11)`: This part iterates through the numbers 1 to 10 (inclusive).
#          The `range()` function generates a sequence of numbers starting from 1 up to 10,
#          but not including, 11.
#       - `x**2`: This is the expression that calculates the square of each number `x`.
#          The `**` operator is the exponentiation operator in Python.



# Exercise 2: Even Numbers
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)

# This code generates a list of even numbers from 1 to 20 using a list comprehension.
# It iterates through numbers from 1 to 20 (`for x in range(1, 21)`)
# and includes only those numbers in the list where the number modulo 2 equals 0 (`if x % 2 == 0`).



# Exercise 3: Uppercase Letters
uppercase_letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
print("Uppercase letters from A to Z:", uppercase_letters)

# This code creates a list of uppercase letters in the English alphabet using a list comprehension.
# It iterates through the ASCII values of uppercase letters from 'A' to 'Z' (inclusive)
# using the `range()` function along with the `ord()` function to get the ASCII value of
# each letter. Then, it converts each ASCII value back to its corresponding character
# using the `chr()` function, and adds it to the list.



# Exercise 4: Length of Words
words = ["apple", "banana", "cherry", "kiwi", "orange"]
word_lengths = [len(word) for word in words]
print("Lengths of words:", word_lengths)

# This code creates a list containing the lengths of words in another list.
# It uses a list comprehension to iterate over each word in the `words` list,
# calculating the length of each word using the `len()` function,
# and then storing these lengths in the `word_lengths` list.




# Exercise 5: Vowel Counter
sentence = "The quick brown fox jumps over the lazy dog"
word_vowel_counts = [sum(1 for char in word if char.lower() in 'aeiou') for word in sentence.split()]
print("Counts of vowels in each word:", word_vowel_counts)

# This code counts the number of vowels in each word of a given sentence.
# It does this by splitting the sentence into individual words
# and then iterating through each word.
# For each word, it counts the number of vowels (letters 'a', 'e', 'i', 'o', 'u')
# using a generator expression and the `sum()` function.
# The result is a list containing the counts of vowels in each word of the sentence.
