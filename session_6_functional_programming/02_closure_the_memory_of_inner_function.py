"""
SESSION 2 CLOSURES
Simple and concept focused
Multiple exercises with solutions
Run section by section

Closure definition
A closure is an inner function that uses variables from an outer function
and still works after the outer function has finished execution

"""

######################################################################
# SECTION 1 RETURNING FUNCTION WITHOUT CLOSURE
# This is only to compare and remove confusion
######################################################################

def get_hello():
    def inner():
        return "Hello"
    return inner

hello_fn = get_hello()
hello_fn()

# NOTE
# inner does not use any outer variable
# so this is not a closure

######################################################################
# SECTION 2 FIRST REAL CLOSURE
######################################################################

def make_adder(n):
    # n is outer variable
    def inner(x):
        # inner uses n so inner is a closure
        return x + n
    return inner

add_10 = make_adder(10)
add_10(5)

add_3 = make_adder(3)
add_3(5)

# EXERCISE 1A
# Create make_multiplier that returns a function
# Returned function should multiply input by n

def make_multiplier(n):
    def inner(x):
        return x * n
    return inner

times_5 = make_multiplier(5)
times_5(4)

# EXERCISE 1B
# Create make_subtractor that returns a function
# Returned function should subtract n from input

def make_subtractor(n):
    def inner(x):
        return x - n
    return inner

minus_2 = make_subtractor(2)
minus_2(10)

######################################################################
# SECTION 3 SHOW THAT THE OUTER FUNCTION IS FINISHED BUT MEMORY REMAINS
######################################################################

def build_message(prefix):
    def inner(name):
        return prefix + " " + name
    return inner

greet_morning = build_message("Good morning")
greet_morning("Sandeep")

# EXERCISE 2A
# Create build_message for "Welcome"
# Store returned function in welcome_user
# Call welcome_user with any name

def build_welcome(prefix):
    def inner(name):
        return prefix + " " + name
    return inner

welcome_user = build_welcome("Welcome")
welcome_user("Amit")

######################################################################
# SECTION 4 CLOSURE WITH MULTIPLE OUTER VARIABLES
######################################################################

def make_full_name_builder(first_name, last_name):
    def inner():
        return first_name + " " + last_name
    return inner

full_name_fn = make_full_name_builder("Sandeep", "Patil")
full_name_fn()

# EXERCISE 3A
# Create make_range_checker(low, high)
# Returned function should check if x is between low and high inclusive
# Test it with low 10 high 20 on values 5 15 25

def make_range_checker(low, high):
    def inner(x):
        return low <= x <= high
    return inner

is_10_to_20 = make_range_checker(10, 20)
is_10_to_20(5)
is_10_to_20(15)
is_10_to_20(25)

######################################################################
# SECTION 5 INSPECTING WHAT A CLOSURE REMEMBERS
######################################################################

def make_prefixer(prefix):
    def inner(text):
        return prefix + text
    return inner

p = make_prefixer("Mr ")
p("Rahul")

# A closure stores its remembered values in __closure__
p.__closure__

# You can inspect the remembered value using cell contents
p.__closure__[0].cell_contents

# EXERCISE 4A
# Create add_7 using make_adder
# Inspect its remembered value using __closure__

add_7 = make_adder(7)
add_7(1)
add_7.__closure__[0].cell_contents

######################################################################
# SECTION 6 COMMON MISTAKE NONLOCAL
# Closures can read outer values easily
# To update outer values, we need nonlocal
######################################################################

def make_counter():
    count = 0
    def inner():
        nonlocal count
        count = count + 1
        return count
    return inner

counter = make_counter()
counter()
counter()
counter()

# EXERCISE 5A
# Create make_down_counter(start)
# Each call should reduce value by 1 and return it
# Use nonlocal
# Test starting from 3

def make_down_counter(start):
    value = start
    def inner():
        nonlocal value
        value = value - 1
        return value
    return inner

down = make_down_counter(3)
down()
down()
down()

######################################################################
# SECTION 7 MULTIPLE CLOSURES ARE INDEPENDENT
######################################################################
def make_counter():
    count = 0
    def inner():
        nonlocal count
        count = count + 1
        return count
    return inner


c1 = make_counter()
c2 = make_counter()

c1()
c1()

c2()
c2()

# NOTE
# c1 and c2 have separate remembered memory

######################################################################
# SECTION 8 CLOSURE IN A LOOP PITFALL AND FIX
# This is a famous closure behavior in Python
######################################################################

def make_multipliers_wrong():
    funcs = []
    for i in [1, 2, 3]:
        def inner(x):
            return x * i
        funcs.append(inner)
    return funcs

wrong = make_multipliers_wrong()
wrong
wrong
wrong

# Explanation
# All inner functions remember the same i
# i becomes 3 at the end of loop
# So all functions behave like multiply by 3

def make_multipliers_right():
    funcs = []
    for i in [1, 2, 3]:
        def inner(x, i=i):
            return x * i
        funcs.append(inner)
    return funcs

right = make_multipliers_right()
right
right
right

# EXERCISE 6A
# Modify make_multipliers_right to create adders instead of multipliers
# It should create functions that add 1 add 2 add 3
# Test on 10

def make_adders_right():
    funcs = []
    for i in [1, 2, 3]:
        def inner(x, i=i):
            return x + i
        funcs.append(inner)
    return funcs

adders = make_adders_right()
adders
adders
adders

######################################################################
# SECTION 9 CLOSURE FOR SIMPLE CACHING
# Keep it minimal and concept focused
######################################################################

def make_square_cache():
    cache = {}
    def inner(x):
        if x in cache:
            return cache[x]
        cache[x] = x * x
        return cache[x]
    return inner

square_cached = make_square_cache()
square_cached(4)
square_cached(4)

# EXERCISE 7A
# Create make_double_cache using same pattern
# It should cache x * 2

def make_double_cache():
    cache = {}
    def inner(x):
        if x in cache:
            return cache[x]
        cache[x] = x * 2
        return cache[x]
    return inner

double_cached = make_double_cache()
double_cached(5)
double_cached(5)

######################################################################
# PART 1 READING OUTER VARIABLE WORKS
######################################################################

def outer_read():
    x = 10

    def inner():
        # Only reading outer variable
        return x

    return inner

f = outer_read()
print(f())  # Works fine


######################################################################
# PART 2 REASSIGNING OUTER VARIABLE FAILS WITHOUT NONLOCAL
######################################################################

def outer_reassign_fail():
    x = 10

    def inner():
        # This line tries to create a NEW local x
        # Python thinks x is local, so reading x before assignment causes error
        # Uncomment to see error
        # x = x + 1
        # return x
        pass

    return inner

# outer_reassign_fail()()  # Would cause error if inner was active


######################################################################
# PART 3 REASSIGNING WITH NONLOCAL WORKS
######################################################################

def outer_reassign_ok():
    x = 10

    def inner():
        nonlocal x  # Tell Python to use outer x
        x = x + 1   # Now we are rebinding outer variable
        return x

    return inner

f = outer_reassign_ok()
print(f())  # 11
print(f())  # 12


######################################################################
# PART 4 MUTATING A DICTIONARY DOES NOT NEED NONLOCAL
######################################################################

def outer_mutation():
    cache = {}  # Outer variable refers to a dictionary

    def inner(key, value):
        # We are NOT doing cache = something_new
        # We are only modifying contents of the same dictionary
        cache[key] = value
        return cache

    return inner

f = outer_mutation()
print(f("a", 1))  # {'a': 1}
print(f("b", 2))  # {'a': 1, 'b': 2}


######################################################################
# PART 5 WHY THIS WORKS
######################################################################

# Variable name = label
# Object = box

# Rebinding:
# cache = {}  -> replacing the box -> needs nonlocal

# Mutation:
# cache["x"] = 1 -> putting item inside same box -> no nonlocal needed

######################################################################
# END OF CLOSURE SCRIPT
######################################################################
