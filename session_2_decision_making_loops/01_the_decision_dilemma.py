# Think of the "if" statement in Python as your code's decision-maker.
# It evaluates a condition and takes one path if the condition is true, and another if it's false.
# Now, when you throw in "else,"
# it's like giving your code a backup plan for when the condition isn't met.
# So, "if" and "else" work together to keep your code flexible and ready for any situation!

# Imagine your little Python program tasked with deciding whether to go out or stay in.
# You check the weather:
#                 - if it's sunny, you'll go out and frolic in the digital meadows;
#                 - if it's rainy, you'll snuggle up inside and binge-watch your favorite shows.

weather = "sunny"

if weather == "sunny": # True
    print("Time to soak up some rays!")
else:
    print("Netflix and chill it is!")

# But wait, there's more! What if the weather could be not just sunny or rainy,
# but also cloudy, snowy,
# or even meteor shower-y? Fear not,
# because Python's got your back with the "elif" clause, short for "else if".
# It's like adding more layers to your decision-making process, making it as complex as you want!

weather = "snowy"

if weather == "sunny":
    print("Time to soak up some rays!")
elif weather == "rainy":
    print("Netflix and chill it is!")
elif weather == "snowy":
    print("Let's build a snowman!")
else:
    print("Let's just stay indoors and contemplate the meaning of life.")
