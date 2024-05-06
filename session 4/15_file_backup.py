# 4. File Backup:
#    Write a Python program that copies the contents of one file to another file,
# creating a backup of the original file.

source_file = "source.txt"
backup_file = "backup.txt"

# Read content from the source file
with open(source_file, "r") as source:
    content = source.read()

# Write content to the backup file
with open(backup_file, "w") as backup:
    backup.write(content)

print("Backup created successfully!")


