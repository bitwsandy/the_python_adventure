# Count Vowels and Consonants :
#   Write a Python program that takes a string as input
#   and counts the number of vowels (a, e, i, o, u) and consonants in the string.
#   Print the counts separately.


input_string = input("Enter a string: ")
# "hello everyone, let's code at 7:00PM"
vowels = 'aeiou'
vowel_count = sum(1 for char in input_string.lower() if char in vowels)
consonant_count = sum(1 for char in input_string.lower() if char.isalpha() and char not in vowels)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

# This code takes a string input from the user and then counts the number of vowels
# and consonants in that string. Here's what it does:
#   - `input_string = input("Enter a string: ")`:
#           This line prompts the user to enter a string, and the input is
#           stored in the variable `input_string`.
#   - `vowels = 'aeiou'`:
#           This variable contains all the lowercase vowels.
#   - `vowel_count = sum(1 for char in input_string.lower() if char in vowels)`:
#           This line counts the number of vowels in the input string.
#           It converts the input string to lowercase (`input_string.lower()`)
#           to make the comparison case-insensitive.
#           Then, it iterates over each character in the string,
#           checking if it's a vowel (using `if char in vowels`).
#           It uses a generator expression to create a sequence of 1s for each vowel,
#           which are then summed up using the `sum()` function.
#   - `consonant_count = sum(1 for char in input_string.lower() if char.isalpha() and char not in vowels)`:
#           This line counts the number of consonants in the input string.
#           It first checks if the character is an alphabet letter (`char.isalpha()`)
#           and if it's not a vowel (`char not in vowels`).
#           Similar to the previous line, it creates a sequence of 1s for
#           each consonant and sums them up.
#   - Finally, it prints the counts of vowels and consonants.


## NERD ZONE :

# Generator expressions and list comprehensions are both allow you to
# create sequences (lists, tuples, etc.) based on some input data or conditions.
# However, there are some key differences between them:
#
# 1. Memory Usage:
#    - List comprehension:
#           When you use a list comprehension, it creates the entire list in memory
#           before returning it.
#           This means that if you have a large input dataset, a list comprehension
#           can consume a lot of memory.
#    - Generator expression:
#           Generators, on the other hand, produce values on-the-fly as you iterate over them.
#           They don't store all the values in memory at once.
#           Instead, they generate values one at a time, which can save memory,
#           especially for large datasets.
#
# 2. Evaluation:
#    - List comprehension:
#           List comprehensions evaluate the entire expression and store the result in memory.
#    - Generator expression:
#           Generators produce values lazily.
#           They only compute the next value when it's needed,
#           making them more efficient for large datasets or when you only need to
#           iterate over the sequence once.
#
# 3. Syntax:
#    -  List comprehension : List comprehensions are surrounded by square brackets `[...]`.
#    -  Generator expression : Generator expressions are surrounded by parentheses `(...)`.
#
# 4. Usage:
#    - Use list comprehensions when you want to create a list and
#       you plan to use that list multiple times or need random access to its elements.
#    - Use generator expressions when you're working with large datasets and
#       want to save memory, or when you only need to iterate over the sequence once.

