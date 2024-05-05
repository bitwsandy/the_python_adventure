# Exercise 1: Squares of Numbers
squares = [x**2 for x in range(1, 11)]
print("Squares of numbers from 1 to 10:", squares)

# Exercise 2: Even Numbers
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)

# Exercise 3: Uppercase Letters
uppercase_letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
print("Uppercase letters from A to Z:", uppercase_letters)

# Exercise 4: Length of Words
words = ["apple", "banana", "cherry", "kiwi", "orange"]
word_lengths = [len(word) for word in words]
print("Lengths of words:", word_lengths)

# Exercise 5: Vowel Counter
sentence = "The quick brown fox jumps over the lazy dog"
word_vowel_counts = [sum(1 for char in word if char.lower() in 'aeiou') for word in sentence.split()]
print("Counts of vowels in each word:", word_vowel_counts)
