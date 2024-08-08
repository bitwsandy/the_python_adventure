# Word Reversal :
#    Write a Python program that takes a sentence as input
#    and reverses the order of words in the sentence.
#    For example, if the input is "hello world", the output should be "world hello".

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print("Reversed sentence:", reversed_sentence)

# This Python program reverses the words in a sentence. Here's a brief explanation:
#
# 1. It prompts the user to enter a sentence.
# 2. It splits the input sentence into words using the `.split()` method,
#    which separates the sentence into a list of words.
# 3. It uses the `reversed()` function to reverse the order of the words in the list.
# 4. It joins the reversed words back together into a single string with spaces between them
#    using `' '.join()`.
# Let's break down `' '.join(reversed(words))`:
#       1. `reversed(words)`:
#           This part uses the `reversed()` function to reverse the order of elements
#           in the `words` list.
#           It returns an iterator that yields the elements of `words` in reverse order.
#       2. `' '.join(...)`:
#           This part joins the elements of an iterable (in this case, the reversed list of words)
#           into a single string, with each element separated by the string `' '`.
#       3. `' '.join(reversed(words))`
#           reverses the order of words in the `words` list and then joins them into
#           a single string with spaces between each word.
#           This effectively creates a reversed version of the input sentence.
# 5. Finally, it prints the reversed sentence.
