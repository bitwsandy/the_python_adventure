# 1. Word Count in a Text File:
#    Write a Python program that reads a text file and counts the number of
# words, lines, and characters in it.
file_name = "example.txt"

with open(file_name, "r") as file:
    # Read the entire file content
    content = file.read()

    # Count the number of words, lines, and characters
    word_count = len(content.split())
    line_count = content.count('\n') + 1
    char_count = len(content)

print(f"Word count: {word_count}")
print(f"Line count: {line_count}")
print(f"Character count: {char_count}")



