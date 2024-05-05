# Foundation :

my_string = "Hello, World!"

for i, char in enumerate(my_string):
    positive_index = i
    negative_index = i - len(my_string)
    print(f"Character: {char}, Positive Index: {positive_index}, Negative Index: {negative_index}")

# The enumerate() function in Python is used to loop over an iterable
# (like a list, tuple, or string) while also keeping track of the index of each item
# in the iterable.
# It returns an enumerate object, which contains pairs of index and item.



# 1. Accessing Individual Characters :

my_string = "Hello, World!"
print(my_string[0])   # Output: H
print(my_string[7])   # Output: W


# 2. Slicing Substrings :

my_string = "Hello, World!"
print(my_string[0:5])     # Output: Hello
print(my_string[7:12])    # Output: World


# 3. Omitting Start or End Index :

my_string = "Hello, World!"
print(my_string[:5])      # Output: Hello
print(my_string[7:])      # Output: World


# 4. Using Negative Indices :

my_string = "Hello, World!"
print(my_string[-6:])     # Output: World
print(my_string[:-7])     # Output: Hello


# 5. Slicing with a Step Size :

my_string = "Hello, World!"
print(my_string[::2])     # Output: Hlo ol!

# In Python, when you use slicing with three colons (`[::2]`),
# it means you're accessing the string with three parameters: `[start:stop:step]`.
# Here's the breakdown of your code:

# - `my_string`: This is the string "Hello, World!".
# - `[::2]`: This slicing syntax is saying:
#   - `start` is not specified, so it starts from the beginning of the string.
#   - `stop` is not specified, so it goes till the end of the string.
#   - `step` is `2`, meaning it selects every second character in the string.




# 6. Reversing a String :

my_string = "Hello, World!"
print(my_string[::-1])    # Output: !dlroW ,olleH

# In Python, when you use slicing with three colons (`[::-1]`),
# it means you're accessing the string with three parameters: `[start:stop:step]`.
# Here's the breakdown:
# - `my_string`: This is the string "Hello, World!".
# - `[::-1]`: This slicing syntax is saying:
#   - `start` is not specified, so it starts from the beginning of the string.
#   - `stop` is not specified, so it goes till the end of the string.
#   - `step` is `-1`, meaning it selects characters in reverse order
# So, `my_string[::-1]` reverses the string "Hello, World!",
# resulting in "!dlroW ,olleH". Each character is selected in reverse order.




# 7. Slicing with Custom Step Size :

my_string = "Hello, World!"
print(my_string[1:10:2])  # Output: el,Wo

# In Python slicing, `my_string[1:10:2]` means:
# - `my_string`: This is the string "Hello, World!".
# - `[1:10:2]`: This slicing syntax is saying:
#   - `start` is `1`, so it starts from the character at index 1 (which is `'e'`).
#   - `stop` is `10`, so it goes up to but does not include the character
#      at index 10 (which is `'d'`).
#   - `step` is `2`, meaning it selects every second character.
# So, `my_string[1:10:2]` selects characters from index 1 to index 9 (not including 10)
# with a step of 2, resulting in "el,Wo".



# 8. Using Variables for Indices :

my_string = "Hello, World!"
start = 2
end = 8
print(my_string[start:end])  # Output: llo, W