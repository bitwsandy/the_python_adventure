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
