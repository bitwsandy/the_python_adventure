# 1. Squares of Numbers
squares = [x ** 2 for x in range(1, 11)]
print("Squares:", squares)

# 2. Even Numbers
even_numbers = [x for x in range(2, 21, 2)]
print("Even Numbers:", even_numbers)

# 3. Words Length
words = ["apple", "banana", "orange", "strawberry"]
word_lengths = [len(word) for word in words]
print("Word Lengths:", word_lengths)

# 4. Vowels in a String
string = "hello world"
vowels_count = sum(1 for char in string if char in 'aeiou')
print("Vowels Count:", vowels_count)

# 5. Prime Numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [x for x in range(2, 51) if is_prime(x)]
print("Prime Numbers:", prime_numbers)

# 6. Matrix Transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Matrix Transpose:", transpose)

# 7. Odd or Even List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_even_list = ['Odd' if x % 2 != 0 else 'Even' for x in numbers]
print("Odd or Even List:", odd_even_list)

# 8. FizzBuzz
fizzbuzz = ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, 101)]
print("FizzBuzz:", fizzbuzz)

# 9. Capitalize Words
words = ["hello", "world", "python", "programming"]
capitalized_words = [word.capitalize() for word in words]
print("Capitalized Words:", capitalized_words)

# 10. Flatten a Nested List
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened List:", flattened_list)
