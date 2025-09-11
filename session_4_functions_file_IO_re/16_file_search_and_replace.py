# 5. File Search and Replace:
#    Write a Python program that reads a text file, searches for a specific string
# or pattern in it, and replaces all occurrences of that string with another string.
file_name = r"C:\Users\Sandeep\Desktop\data\wordcount.txt"

# Read content from the file
with open(file_name, "r") as file:
    content = file.read()

# Search for a specific string and replace it
search_string = "nifi"
replace_string = "hadoop"
new_content = content.replace(search_string, replace_string)

# Write the modified content back to the file
with open(file_name, "w") as file:
    file.write(new_content)

print("Search and replace completed successfully!")
