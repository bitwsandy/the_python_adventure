# Word Reversal :
#    Write a Python program that takes a sentence as input
#    and reverses the order of words in the sentence.
#    For example, if the input is "hello world", the output should be "world hello".

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print("Reversed sentence:", reversed_sentence)