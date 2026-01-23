"""
SESSION 1 FUNCTIONAL PROGRAMMING FOUNDATIONS

Concepts covered
Function object basics
Function aliases
Passing function as an argument
Returning function from another function
Simple higher order functions
Introduction to lambda

Teaching instruction
Run section by section
Ask students to predict output before running
Focus on WHAT is happening, not HOW complex the logic is
"""

######################################################################
# SECTION 1 FUNCTION OBJECT BASICS
######################################################################

def add(a, b):
    return a + b

# A function is an object in Python
# It has a type and identity just like int or str
print(type(add))

# Storing function object in another variable
ref = add  # No brackets means function is not called

add(2, 3)
ref(2, 3)

print(type(add))
print(type(ref))

# Both names point to the same function object
print(add is ref)


# EXERCISE 1A
# Create a function named multiply that returns a * b
# Print the type of multiply
# Store multiply in variable m
# Call m(3, 4)

def multiply(a, b):
    return a * b

print(type(multiply))
m = multiply
m(3, 4)


# EXERCISE 1B
# Create a function named greet_user that returns Hello plus name
# Store it in variable another_name
# Call another_name with any name

def greet_user(name):
    return "Hello " + name

another_name = greet_user
another_name("Amit")


# EXERCISE 1C
# Check whether greet_user and another_name point to the same object

print(greet_user is another_name)


######################################################################
# SECTION 2 FUNCTION ALIASES
######################################################################

def greet(name):
    return "Hello " + name

# Creating alias
hello = greet

greet("Sandeep")
hello("Sandeep")

# Both names point to same function object
print(greet is hello)


# EXERCISE 2A
# Create an alias hi for greet
# Call hi("Neha")
# Check greet is hi

hi = greet
hi("Neha")
print(greet is hi)


# EXERCISE 2B
# Create one more alias named welcome
# Call welcome("Rahul")
# Check hi is welcome

welcome = greet
welcome("Rahul")
print(hi is welcome)


# EXERCISE 2C
# Reassign hi to point to add
# Call hi(2, 3)
# Observe that labels can be reassigned
def add(a, b):
    return a + b

hi = add
hi(2, 3)


######################################################################
# SECTION 3 PASSING FUNCTION AS AN ARGUMENT | HOF
######################################################################

def apply_operation(operation, x, y):
    # operation is a function
    # behavior is passed as data
    return operation(x, y)

def subtract(a, b):
    return a - b

apply_operation(add, 10, 5)
apply_operation(subtract, 10, 5)


# EXERCISE 3A
# Create a function maximum that returns larger value
# Pass it to apply_operation

def maximum(a, b):
    if a > b:
        return a
    return b

apply_operation(maximum, 8, 12)


# EXERCISE 3B
# Create a function minimum that returns smaller value
# Pass it to apply_operation

def minimum(a, b):
    if a < b:
        return a
    return b

apply_operation(minimum, 8, 12)


# EXERCISE 3C
# Create a function describe_function
# It should accept a function and return its name as string
def add(a, b):
    return a + b

def describe_function(fn):
    return fn.__name__

describe_function(add)
describe_function(subtract)


######################################################################
# SECTION 4 RETURNING FUNCTION FROM ANOTHER FUNCTION
######################################################################

# In this section, focus only on this idea
# A function can return another function


def get_hello_function():
    # This function creates another function
    # It does not remember anything from get_hello_function
    def say_hello():
        return "Hello"
    return say_hello  # returning function, not calling it


# get_hello_function returns a function
hello_fn = get_hello_function() # say_hello

# hello_fn is now a function
hello_fn()


# EXERCISE 4A
# Create a function named get_welcome_function
# Inside it, define a function named welcome
# welcome should return "Welcome"
# Return the welcome function
# Call the returned function and observe the output

def get_welcome_function():
    def welcome():
        return "Welcome"
    return welcome

welcome_fn = get_welcome_function() # Welcome
welcome_fn()


# EXERCISE 4B
# Create a function named get_number_function
# Inside it, define a function that returns number 100
# Return the inner function
# Store the returned function in a variable and call it

def get_number_function():
    def give_number():
        return 100
    return give_number

number_fn = get_number_function()
number_fn()


# EXERCISE 4C
# Create a function named choose_function
# If input text is "add", return the add function
# If input text is "sub", return the subtract function
# Do NOT create any inner function here
# Call the returned function normally

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def choose_function(text):
    if text == "add":
        return add
    if text == "sub":
        return subtract
    return add

chosen = choose_function("add")
chosen(5, 3)


# EXERCISE 4D
# Create a function named get_printer
# It should return a function that prints "Done"
# Call the returned function

def get_printer():
    def printer():
        print("Done")
    return printer

printer_fn = get_printer()
printer_fn()


######################################################################
# SECTION 5 SIMPLE HIGHER ORDER FUNCTION
######################################################################

def transform_list(items, transformer):
    result = []
    for item in items:
        result.append(transformer(item))
    return result

def plus_one(x):
    return x + 1

transform_list([1, 2, 3], plus_one)


# EXERCISE 5A
# Create to_string function
# Use transform_list on [10, 20, 30]

def to_string(x):
    return str(x)

transform_list([10, 20, 30], to_string)


# EXERCISE 5B
# Create is_even function
# Use transform_list on [1, 2, 3, 4]

def is_even(x):
    return x % 2 == 0

transform_list([1, 2, 3, 4], is_even)


# EXERCISE 5C
# Create apply_twice function
# It should apply function twice on value

def apply_twice(fn, value):
    return fn(fn(value))

apply_twice(plus_one, 10)


######################################################################
# SECTION 6 INTRODUCTION TO LAMBDA
######################################################################
######################################################################
# SECTION 6 INTRODUCTION TO LAMBDA
# Self contained
# No closure
# No dependency on other sections
######################################################################

# lambda creates a small anonymous function in one line
# It is equivalent to a very small normal function

double = lambda x: x * 2
double(5)


# EXERCISE 6A
# Create a lambda named square
# It should return square of a number
# Test with 4

square = lambda x: x * x
square(4)


# EXERCISE 6B
# Create a lambda named add
# It should take two numbers and return their sum
# Test with 3 and 7

add = lambda a, b: a + b
add(3, 7)


# EXERCISE 6C
# Create a lambda named is_even
# It should return True if number is even else False
# Test with 4 and 5

is_even = lambda x: x % 2 == 0
is_even(4)
is_even(5)


# EXERCISE 6D
# Create a lambda named to_string
# It should convert a number to string
# Test with 10

to_string = lambda x: str(x)
to_string(10)


# EXERCISE 6E
# Create a lambda named max_value
# It should return bigger of two numbers
# Test with 8 and 12

max_value = lambda a, b: a if a > b else b
max_value(8, 12)


# IMPORTANT NOTE
# lambda should be used only for small, simple expressions
# If logic grows, use def instead
# Avoid using outer variables in lambda in Session 1

######################################################################
# END OF SESSION 1
######################################################################

# HIGHER ORDER FUNCTIONS QUICK USAGE GUIDE
#
# PASSING FUNCTION AS AN ARGUMENT
#
# Use this when the flow of execution is fixed
# and only the behavior needs to change.
# The outer function controls when and how the function is executed.
# Best for transformation pipelines, validation rules, and strategy selection.
# Common in data processing, callbacks, sorting, filtering, and frameworks.
# Think same process, different behavior.


# RETURNING A FUNCTION
#
# Returning a function is used when
# we want to build or configure behavior first
# and execute it later.

# The outer function does not perform the final action.
# It prepares a function based on input arguments.

# The returned function is executed later,
# possibly many times.

# The same higher order function can be reused
# to create multiple prepared functions
# with different behavior.

# Best for factory patterns, decorators, delayed execution, and configuration based logic.
# Common in logging wrappers, authentication layers, and workflow builders.
# Think build behavior now, execute later.


