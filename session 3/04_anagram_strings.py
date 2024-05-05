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
