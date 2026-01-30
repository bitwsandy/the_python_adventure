"""
SESSION ITERATORS

Focus
Understanding iterables and iterators
How for loop works internally
How generators relate to iterators
Building custom iterator

Key idea
Generator is a shortcut
Iterator is the real mechanism
"""

######################################################################
# SECTION 1 WHAT IS AN ITERABLE
######################################################################

numbers = [1, 2, 3]

# List is iterable
# It can be used in a for loop
for n in numbers:
    print(n)


######################################################################
# SECTION 2 CONVERT ITERABLE TO ITERATOR
######################################################################

it = iter(numbers)

# Now it is an iterator
it


######################################################################
# SECTION 3 USING NEXT ON ITERATOR
######################################################################

next(it)
next(it)
next(it)
# next(it) again would raise StopIteration


######################################################################
# SECTION 4 FOR LOOP INTERNAL MECHANISM
######################################################################

it = iter(numbers)

while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break

# This is how for loop works internally


######################################################################
# SECTION 5 GENERATOR IS AN ITERATOR
######################################################################

def gen_numbers():
    yield 1
    yield 2
    yield 3

g = gen_numbers()

# Generator is already an iterator
next(g)
next(g)
next(g)


######################################################################
# SECTION 6 CUSTOM ITERATOR CLASS
######################################################################

class MyIterator:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 3:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

obj = MyIterator()

for n in obj:
    print(n)


######################################################################
# EXERCISE 1 SIMPLE CUSTOM ITERATOR
# Create class CountToFive that iterates from 1 to 5
######################################################################

class CountToFive:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

c = CountToFive()
for n in c:
    print(n)


######################################################################
# EXERCISE 2 STRING ITERATOR
# Create iterator that goes through characters of "HELLO"
######################################################################

class StringIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration

s = StringIterator("HELLO")
for ch in s:
    print(ch)


######################################################################
# EXERCISE 3 SQUARE ITERATOR
# Iterator that returns squares of 1 to 4
######################################################################

class SquareIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 4:
            value = self.num * self.num
            self.num += 1
            return value
        else:
            raise StopIteration

sq = SquareIterator()
for v in sq:
    print(v)


######################################################################
# SECTION 7 ANALOGY
#
# Book Pages
# Iterable is the book
# Iterator is the bookmark moving page by page
# next() moves to next page
######################################################################
