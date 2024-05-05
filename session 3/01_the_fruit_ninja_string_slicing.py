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


# 6. Reversing a String :

my_string = "Hello, World!"
print(my_string[::-1])    # Output: !dlroW ,olleH


# 7. Slicing with Custom Step Size :

my_string = "Hello, World!"
print(my_string[1:10:2])  # Output: el,Wo


# 8. Using Variables for Indices :

my_string = "Hello, World!"
start = 2
end = 8
print(my_string[start:end])  # Output: llo, W