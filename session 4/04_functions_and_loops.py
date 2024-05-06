# Prime Numbers in a Range:
# Write a function that takes a range of numbers as input and returns
# a list of prime numbers within that range.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    prime_nums = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_nums.append(num)
    return prime_nums

# Test the function
print(prime_numbers_in_range(10, 30))  # Output: [11, 13, 17, 19, 23, 29]



# Multiplication Table:
# Write a function that generates the multiplication table up to a specified number.
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end="\t")
        print()
# Test the function
multiplication_table(5)



# Calculate Average:
# Write a function that takes a list of numbers as input and
# returns the average of those numbers.
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers) if numbers else 0
# Test the function
print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0


# Factorial of Each Number:
# Write a function that takes a list of numbers as input and
# returns a list of factorials for each number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorials_of_numbers(nums):
    factorials = []
    for num in nums:
        factorials.append(factorial(num))
    return factorials
# Test the function
print(factorials_of_numbers([1, 2, 3, 4, 5]))  # Output: [1, 2, 6, 24, 120]



# Count Characters:
# Write a function that takes a string and counts the occurrence of each character,
# then returns a dictionary with characters as keys and their counts as values.
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
# Test the function
print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
