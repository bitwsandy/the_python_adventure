import os
import datetime
import math
import random
import sys

# Exercise 1: File Manipulation with os Module
def list_files_in_directory(directory):
    if __name__ == '__main__' :
        """List all the files in the specified directory."""
        files = os.listdir(directory)
        for file in files:
            print(file)

# Exercise 2: Date and Time Manipulation with datetime Module
def calculate_date_difference(date1, date2):
    """Calculate the difference in days between two dates."""
    delta = date2 - date1
    print("Difference in days:", delta.days)

# Exercise 3: Math Operations with math Module
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    area = math.pi * math.pow(radius, 2)
    print("Area of the circle:", area)

# Exercise 4: Random Number Generation with random Module
def generate_random_password(length):
    """Generate a random password of specified length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Random Password:", password)

# Exercise 5: Working with Command-Line Arguments using sys Module
def get_file_size(filename):
    """Get the size of a file in bytes."""
    size = os.path.getsize(filename)
    print("File Size:", size, "bytes")

# Testing the functions
if __name__ == "__main__":
    # Exercise 1
    print("\nExercise 1: File Manipulation with os Module")
    list_files_in_directory(".")  # List files in the current directory

    # Exercise 2
    print("\nExercise 2: Date and Time Manipulation with datetime Module")
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 12, 31)
    calculate_date_difference(date1, date2)

    # Exercise 3
    print("\nExercise 3: Math Operations with math Module")
    calculate_circle_area(5)

    # Exercise 4
    print("\nExercise 4: Random Number Generation with random Module")
    generate_random_password(10)

    # Exercise 5
    print("\nExercise 5: Working with Command-Line Arguments using sys Module")
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        filename = sys.argv[1]
        get_file_size(filename)
