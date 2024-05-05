# Loops in Python are like magical spells that let you repeat tasks
# without having to write the same code over and over again.
# They're incredibly handy for
# automating repetitive tasks and processing large amounts of data efficiently.

# Python offers two main types of loops: the "for" loop and the "while" loop.

# 1. For Loop:
#   The "for" loop is like a tour guide taking you through a list, one item at a time.
#   It iterates over a sequence (such as a list, tuple, string, or range)
#   and executes the block of code for each item in the sequence.

# 2. While Loop:
#   The "while" loop is like a guard dog,
#   repeating a block of code as long as a specified condition is true.
#   It keeps looping until the condition becomes false.

# In following example, the loop iterates over each item in the list of fruits
# and prints each fruit.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("For loop printer : ", x)

index = 0
while index < len(fruits):
    print("While loop printer : ",fruits[index])
    index += 1

print("\n")

# In following example, the loop continues printing the value of `count`
# as long as it's less than 5.
# Once `count` reaches 5 or more, the loop stops.

count = 0
while count < 5:
    print("While loop printer : ",count)
    count += 1

for count in range(5):
    print("For loop printer",count)



