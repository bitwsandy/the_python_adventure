
# Count Vowels:
#    Write a function that takes a string as input and returns the count of vowels in that string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test the function
print(count_vowels("Hello World"))  # Output: 3



# Factorial:
#    Write a function to calculate the factorial of a given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120



# Fibonacci Sequence:
#    Write a function to generate the Fibonacci sequence up to a specified number of terms.
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Test the function
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



# Palindrome Checker:
#    Write a function that checks whether a given string is a palindrome or not.
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# Return Multiple values
def calc(a,b):
    return a+b, a-b, a*b, a/b

# def calc(a,b):
#     return a+b
#     return a-b
#     return a*b
#     return a/b

sum, sub, mult, div = calc(10,5)
print(sum, sub, mult, div)




