# 1. Opening a File:
# To work with a file, you first need to open it. You can open a file using the open()
# function. You need to provide the file name and the mode in which you want to open
# the file (read, write, or append). For example:

file = open("example.txt", "r")  # Open the file "example.txt" in read mode


# 2. Reading from a File:
# Once the file is open, you can read its contents. There are several methods
# to read from a file:
#    - read(): Reads the entire file as a single string.
#    - readline(): Reads a single line from the file.
#    - readlines(): Reads all lines from the file and returns them as a list.

content = file.read()  # Read the entire file content
line = file.readline()  # Read a single line from the file
lines = file.readlines()  # Read all lines from the file


# 3. Writing to a File:
#         You can also write to a file by opening it in write mode ("w") or append
# mode ("a"). If the file doesn't exist, Python will create it for you. Be careful,
# as opening a file in write mode will overwrite its existing content.

file = open("example.txt", "w")  # Open the file "example.txt" in write mode
file.write("Hello, World!")  # Write to the file


# 4. Closing a File:
#         After you're done working with a file, it's important to close it using the
# close() method. This ensures that any resources associated with the file are properly
# released.

file.close()  # Close the file


# 5. Context Managers:
#         To ensure that files are properly closed even if an error occurs,
# you can use a context manager (with statement). This automatically closes the
# file when you're done with it.

with open("example.txt", "r") as file:
    content = file.read()  # Read the file content
    print(content)
# File is automatically closed when you exit the 'with' block


# 6. Append Content to a File:
#    Write a Python program that appends a line of text to an existing file.

# Open the file in append mode
with open("example.txt", "a") as file:
    # Prompt the user to enter text to append
    text = input("Enter text to append: ")
    # Append the text to the file
    file.write(text + "\n")
    print("Text appended to file successfully!")


# 7. Delete Content of a File:
#    Write a Python program that deletes the content of an existing file.

# Open the file in write mode, which will clear its existing content
with open("example.txt", "w") as file:
    # Write an empty string to the file
    file.write("")
    print("Content of file deleted successfully!")

