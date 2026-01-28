"""
SESSION 3 DECORATORS

Focus
Understanding decorators step by step
No complex logic
Closures used naturally

Flow
1 Manual wrapping
2 Wrapper pattern
3 Real decorator
4 Decorator syntax
5 Multiple exercises
"""

######################################################################
# SECTION 1 FUNCTION WITHOUT DECORATOR
######################################################################

def say_hello():
    print("Hello")

say_hello()

# Problem
# What if we want to print something before and after every function?


######################################################################
# SECTION 2 MANUAL WRAPPING
######################################################################

def manual_wrapper(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def greet():
    print("Hi")

greet = manual_wrapper(greet)
greet()

# We wrapped greet manually


######################################################################
# SECTION 3 SIMPLE DECORATOR
######################################################################

def simple_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def hello():
    print("Hello World")

hello = simple_decorator(hello)
hello()


######################################################################
# SECTION 4 DECORATOR SYNTAX
######################################################################

def simple_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@simple_decorator
def say_hi():
    print("Hi")

say_hi()


######################################################################
# SECTION 5 DECORATOR WITH RETURN VALUE
######################################################################

def result_decorator(func):
    def wrapper():
        print("Calculating")
        result = func()
        print("Done")
        return result
    return wrapper

@result_decorator
def get_number():
    return 10

print(get_number())


######################################################################
# SECTION 6 DECORATOR WITH ARGUMENTS
######################################################################

def log_decorator(func):
    def wrapper(a, b):
        print("Inputs are", a, b)
        return func(a, b)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(3, 4))


######################################################################
# SECTION 7 MULTIPLE DECORATORS
######################################################################

def deco1(func):
    def wrapper():
        print("Deco1")
        func()
    return wrapper

def deco2(func):
    def wrapper():
        print("Deco2")
        func()
    return wrapper

@deco1
@deco2
def greet_user():
    print("Hello User")

greet_user()


######################################################################
# EXERCISE 1 BASIC DECORATOR
# Create a decorator that prints "Running function"
# Apply it to a function that prints "Task done"
######################################################################

def running_decorator(func):
    def wrapper():
        print("Running function")
        func()
    return wrapper

@running_decorator
def task():
    print("Task done")

task()


######################################################################
# EXERCISE 2 DECORATOR THAT COUNTS CALLS
######################################################################

def call_counter(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("Called", count, "times")
        func()
    return wrapper

@call_counter
def greet_again():
    print("Hello")

greet_again()
greet_again()
greet_again()


######################################################################
# EXERCISE 3 TIMING DECORATOR
######################################################################

import time

def timing_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken", end - start)
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)

slow_function()


######################################################################
# EXERCISE 4 AUTHORIZATION STYLE DECORATOR
######################################################################

def auth_decorator(func):
    def wrapper(user):
        if user == "admin":
            func(user)
        else:
            print("Access denied")
    return wrapper

@auth_decorator
def dashboard(user):
    print("Welcome to dashboard", user)

dashboard("admin")
dashboard("guest")


######################################################################
# END OF DECORATOR SCRIPT
######################################################################
