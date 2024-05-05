# Title Capitalization:
#    Write a Python function that takes a sentence as input
#    and capitalizes the first letter of each word, except for articles,
#    conjunctions, and prepositions (e.g., "the", "and", "in").
#    Print the capitalized sentence.


sentence = input("Enter a sentence: ")
articles = ['a', 'an', 'the']
conjunctions = ['and', 'but', 'or', 'nor', 'for', 'yet', 'so']
prepositions = ['in', 'on', 'at', 'by', 'to', 'of', 'with']
title_case_sentence = ' '.join(word.capitalize() if word.lower() not in articles + conjunctions + prepositions else word for word in sentence.split())
print("Title case sentence:", title_case_sentence)
