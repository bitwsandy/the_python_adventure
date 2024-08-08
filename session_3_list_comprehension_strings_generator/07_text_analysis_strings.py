# Text Analysis :
#    Create a Python program that analyzes a piece of text and prints
#    the following statistics:
#    - Number of characters (including spaces and punctuation)
#    - Number of words
#    - Number of sentences
#    - Average word length
#    - Average sentence length (in terms of words)


text = input("Enter a piece of text: ")
num_chars = len(text)
num_words = len(text.split())
num_sentences = text.count('.') + text.count('!') + text.count('?')
avg_word_length = sum(len(word) for word in text.split()) / num_words
avg_sentence_length = num_words / num_sentences

print("Number of characters:", num_chars)
print("Number of words:", num_words)
print("Number of sentences:", num_sentences)
print("Average word length:", avg_word_length)
print("Average sentence length:", avg_sentence_length)

# This Python code analyzes a piece of text entered by the user to calculate various statistics:

# 1. `num_chars = len(text)`:
#       It calculates the number of characters in the input text by using the `len()` function.
#
# 2. `num_words = len(text.split())`:
#       It calculates the number of words in the input text by splitting the text
#       into words using the `.split()` method and then counting the number of resulting elements.
#
# 3. `num_sentences = text.count('.') + text.count('!') + text.count('?')`:
#       It calculates the number of sentences in the input text by counting the occurrences
#       of period ('.'), exclamation mark ('!'), and question mark ('?').
#
# 4. `avg_word_length = sum(len(word) for word in text.split()) / num_words`:
#       It calculates the average word length by summing the length of each word in
#       the text and dividing by the total number of words.
#
# 5. `avg_sentence_length = num_words / num_sentences`:
#       It calculates the average sentence length by dividing the total number
#       of words by the total number of sentences.
#