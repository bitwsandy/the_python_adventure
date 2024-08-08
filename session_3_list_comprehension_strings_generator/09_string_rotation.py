# String Rotation :
#    Write a Python program that takes two strings as input
#    and checks if one string is a rotation of the other.
#    For example, consider the string "hello":
#           One rotation of "hello" would result in "ohell"
#           (moving the last character 'o' to the beginning).
#           Another rotation would result in "lohel".
#           And so on, until returning to the original string "hello".

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) != len(string2):
    print("No, the strings are not rotations of each other.")
else:
    if string1 in (string2 + string2):
        print("Yes, one string is a rotation of the other.")
    else:
        print("No, the strings are not rotations of each other.")

# This Python code checks if two strings are rotations of each other. Here's a brief explanation:
#
# 1. It prompts the user to enter two strings.
# 2. It checks if the lengths of the two strings are not equal.
#    If they are not equal, it prints that the strings are not rotations of each other.
# 3. If the lengths are equal, it checks if `string1` is a substring of the concatenation
#    of `string2` with itself.
#    If it is, it prints that one string is a rotation of the other;
#    otherwise, it prints that the strings are not rotations of each other.
#
