# string_operations.py
import os
def list_files_in_directory(directory):
        """List all the files in the specified directory."""
        files = os.listdir(directory)
        for file in files:
            print(file)

def capitalize_string(s):
    return s.capitalize()

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def concatenate_strings(str1, str2):
    try:
        result = str1 + str2
        return result
    except TypeError:
        return "Error: Cannot concatenate strings."


