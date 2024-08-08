# Word Frequency Counter:
#   Write a Python program that takes a paragraph of text as input
#   and counts the frequency of each word in the text.
#   Print the word frequencies in descending order.

# Dictionaries

paragraph = input("Enter a paragraph of text: ")
words = paragraph.split()
word_freq = {}
for word in words:
    word = word.lower()
    word_freq[word] = word_freq.get(word, 0) + 1
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, freq in sorted_word_freq:
    print(f"{word}: {freq}")

# This Python program counts the frequency of each word in a paragraph of text
# entered by the user and then prints the words along with their frequencies in descending order.
# Here's a breakdown:
#
# 1. It prompts the user to enter a paragraph of text.
# 2. It splits the input paragraph into words using the `.split()` method,
#    which separates the paragraph into a list of words.
# 3. It initializes an empty dictionary `word_freq` to store the frequency of each word.
# 4. It iterates through each word in the list of words:
#    - It converts each word to lowercase using `.lower()` to make the comparison case-insensitive.
#    - It updates the `word_freq` dictionary by incrementing the count for the current word
#      using `.get()` method.
#      If the word is not already in the dictionary, it initializes its count to 0 and
#      then increments it by 1.
# 5. It sorts the `word_freq` dictionary based on the frequency of words in descending order
#    using the `sorted()` function and a lambda function as the sorting key.
# 6. It iterates through the sorted word-frequency pairs (`sorted_word_freq`) and prints
#    each word along with its frequency.
#






