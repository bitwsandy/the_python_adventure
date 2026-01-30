"""
SESSION GENERATORS

Focus
Understanding generators and yield
How execution pauses and resumes
Why generators save memory

Function that gives everything vs function that gives step by step
"""

######################################################################
# SECTION 1 NORMAL FUNCTION
######################################################################

def normal_numbers():
    return [1, 2, 3]

# Returns everything at once
normal_numbers()


######################################################################
# SECTION 2 GENERATOR FUNCTION
######################################################################

def gen_numbers():
    yield 1
    yield 2
    yield 3

g = gen_numbers()

# Generator does not run immediately
g


######################################################################
# SECTION 3 USING NEXT TO PULL VALUES
######################################################################

next(g)
next(g)
next(g)
# next(g) would now cause StopIteration


######################################################################
# SECTION 4 USING FOR LOOP
######################################################################

for n in gen_numbers():
    print(n)

# for loop automatically calls next() internally


######################################################################
# SECTION 5 EXECUTION PAUSES
######################################################################

def gen_demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

g = gen_demo()

next(g)
next(g)
next(g)


######################################################################
# SECTION 6 GENERATOR VS LIST
######################################################################

def list_function():
    return [i for i in range(5)]

def generator_function():
    for i in range(5):
        yield i

list_function()
generator_function()


######################################################################
# EXERCISE 1 SIMPLE GENERATOR
# Create a generator that yields 10, 20, 30
######################################################################

def gen_values():
    yield 10
    yield 20
    yield 30

for v in gen_values():
    print(v)


######################################################################
# EXERCISE 2 GENERATOR WITH LOOP
# Create generator that yields numbers 1 to 5
######################################################################

def gen_1_to_5():
    for i in range(1, 6):
        yield i

for n in gen_1_to_5():
    print(n)


######################################################################
# EXERCISE 3 SQUARE GENERATOR
# Generator should yield squares of numbers 1 to 4
######################################################################

def gen_squares():
    for i in range(1, 5):
        yield i * i

for s in gen_squares():
    print(s)


######################################################################
# EXERCISE 4 GENERATOR EXPRESSION
######################################################################

g = (i * 2 for i in range(5))
for v in g:
    print(v)


######################################################################
# EXERCISE 5 GENERATOR THAT STOPS BASED ON CONDITION
# Yield numbers until number becomes 4
######################################################################

def gen_until_4():
    for i in range(10):
        if i == 4:
            return
        yield i

for n in gen_until_4():
    print(n)


######################################################################
# SECTION 7 MEMORY IDEA
######################################################################

# List stores all values in memory
big_list = [i for i in range(1000000)]

# Generator does not store all values
big_gen = (i for i in range(1000000))


######################################################################
# SECTION 8 REAL WORLD ANALOGY
#
# Water Tap
# Normal function = full bucket
# Generator = water flows only when needed
######################################################################
