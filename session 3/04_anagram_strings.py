# Anagram Checker :
#    Write a Python program that checks whether two given strings are
#    anagrams of each other.
#    An anagram is a word or phrase formed by rearranging the letters
#    of another word or phrase,
#    typically using all the original letters exactly once.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string1 = string1.lower().replace(" ", "")
string2 = string2.lower().replace(" ", "")
if sorted(string1) == sorted(string2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")


# This Python program checks whether two strings are anagrams of each other.
# Here's a brief explanation of how it works:

# 1. It prompts the user to enter two strings.
# 2. It converts both input strings to lowercase using `.lower()` to make
#    the comparison case-insensitive.
# 3. It removes any spaces from both input strings using `.replace(" ", "")`.
# 4. It checks if the sorted version of both strings (`sorted(string1)` and `sorted(string2)`)
#    are equal.
#    If they are equal, it means the two strings contain the same characters in the same frequency,
#    which indicates that they are anagrams.
#    In that case, it prints "They are anagrams!". Otherwise, it prints "They are not anagrams."
