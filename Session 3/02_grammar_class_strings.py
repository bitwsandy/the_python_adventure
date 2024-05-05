# Count Vowels and Consonants :
#   Write a Python program that takes a string as input
#   and counts the number of vowels (a, e, i, o, u) and consonants in the string.
#   Print the counts separately.


input_string = input("Enter a string: ")
vowels = 'aeiou'
vowel_count = sum(1 for char in input_string.lower() if char in vowels)
consonant_count = sum(1 for char in input_string.lower() if char.isalpha() and char not in vowels)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)