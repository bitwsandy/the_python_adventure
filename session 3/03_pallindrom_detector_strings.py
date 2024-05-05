# Palindrome Checker :
#    Write a Python program that checks whether a given string is a palindrome or not.
#    A palindrome is a word, phrase, number, or other sequence of characters
#    that reads the same backward as forward.
#    Ignore spaces, punctuation, and capitalization.

input_string = input("Enter a string: ")
input_string = input_string.lower().replace(" ", "").replace(".", "").replace(",", "")
if input_string == input_string[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

# This Python program checks whether a given string is a palindrome or not. Here's how it works:
#
# 1. It prompts the user to enter a string.
# 2. It converts the input string to lowercase using `lower()` to make
#    the comparison case-insensitive.
# 3. It removes any spaces, dots, and commas from the input string using `replace()` method calls.
# 4. It checks if the modified input string is equal to its reverse
#    (`input_string[::-1]`).
#    If they are equal, it prints "It's a palindrome!",
#    indicating that the input string reads the same forwards and backwards.
#    Otherwise, it prints "It's not a palindrome."
