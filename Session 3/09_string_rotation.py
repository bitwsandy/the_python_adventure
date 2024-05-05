# String Rotation :
#    Write a Python program that takes two strings as input
#    and checks if one string is a rotation of the other.
#    For example, consider the string "hello":
#           One rotation of "hello" would result in "ohell"
#           (moving the last character 'o' to the beginning).
#           Another rotation would result in "lohel".
#           And so on, until returning to the original string "hello".

def is_rotation(string1, string2):
    if len(string1) != len(string2):
        return False
    return string1 in (string2 + string2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if is_rotation(string1, string2):
    print("Yes, one string is a rotation of the other.")
else:
    print("No, the strings are not rotations of each other.")
