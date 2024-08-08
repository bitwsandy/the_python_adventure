# using following code I can print four values, variable, expression, Combination or ()
formatter = "{} {} {} {}"

s1 = "Hello World"

print(formatter.format(1, 2, 3, 4))
#print("{} {} {} {}".format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format("one", 2, "three", 4))
print(formatter.format(True, 2, False, "four"))
print(formatter.format("one", 2,s1, 4+5-2*2))
print(formatter.format(formatter, formatter, formatter, formatter))
#
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
