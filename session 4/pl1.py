import sys

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result of division:", result)
finally:
    print("I don't care if error occurs on not, I'll get executed anyways")

