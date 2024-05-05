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