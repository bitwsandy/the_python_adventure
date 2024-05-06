# Word Frequency Counter:
# Write a function that takes a string of text as input and returns
# a dictionary where keys are words and values are the frequencies of those words in the text.
# Ignore punctuation and consider case-insensitive.
import string

def word_frequency(text):
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.lower().split()  # Convert to lowercase and split into words
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Test the function
print(word_frequency("This is a test. This test is for word frequency test."))
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 3, 'for': 1, 'word': 1, 'frequency': 1}



# FizzBuzz:
# Write a function that takes a number n as input and prints the numbers from 1 to n, but for multiples of 3, print "Fizz" instead of the number,
# for multiples of 5, print "Buzz", and for multiples of both 3 and 5, print "FizzBuzz".
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test the function
fizz_buzz(15)



# GCD (Greatest Common Divisor):
# Write a function that calculates the greatest common divisor (GCD)
# of two numbers using the Euclidean algorithm.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
print(gcd(48, 18))  # Output: 6



# Sum of Digits:
# Write a function that takes a number as input
# and returns the sum of its digits.
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

# Test the function
print(sum_of_digits(12345))  # Output: 15


# Password Strength Checker:
# Write a function that takes a password as input and checks its strength
# based on the following criteria:
# - At least 8 characters long
# - Contains both uppercase and lowercase letters
# - Contains at least one digit
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long"
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter"
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit"
    return "Strong"

# Test the function
print(check_password_strength("Password123"))  # Output: "Strong"
