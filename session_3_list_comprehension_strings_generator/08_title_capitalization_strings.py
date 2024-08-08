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


# This Python code converts a sentence entered by the user into title case,
# with certain exceptions for articles, conjunctions, and prepositions. Here's how it works:
#
# 1. It prompts the user to enter a sentence.
# 2. It splits the input sentence into words using the `.split()` method.
# 3. It iterates over each word in the split sentence.
# 4. For each word, it checks if it is not in the lists of articles,
#    conjunctions, or prepositions.
#    If it's not in any of these lists,
#    it capitalizes the first letter of the word using `.capitalize()`.
# 5. It joins the modified words back together into a single sentence
#    with spaces between them using `' '.join(...)`.
# 6. Finally, it prints the title case sentence.
#