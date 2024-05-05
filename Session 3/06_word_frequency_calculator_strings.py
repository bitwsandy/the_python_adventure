# Word Frequency Counter:
#   Write a Python program that takes a paragraph of text as input
#   and counts the frequency of each word in the text.
#   Print the word frequencies in descending order.


paragraph = input("Enter a paragraph of text: ")
words = paragraph.split()
word_freq = {}
for word in words:
    word = word.lower()
    word_freq[word] = word_freq.get(word, 0) + 1
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, freq in sorted_word_freq:
    print(f"{word}: {freq}")







