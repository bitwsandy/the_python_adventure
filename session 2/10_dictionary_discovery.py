# Initialize an empty dictionary
database = {}

# Adding entries to the dictionary
database['001'] = {'Name': 'Alice', 'Age': '20', 'Course': 'Biology'}
database['002'] = {'Name': 'Bob', 'Age': '22', 'Course': 'Chemistry'}

# Display the dictionary
print("Initial Database:")
print(database)

# Updating an entry
database['001']['Age'] = '21'  # Update Alice's age
database['003'] = {'Name': 'Charlie', 'Age': '23', 'Course': 'Mathematics'}  # Add a new student

# Accessing an entry
print("\nUpdated Database:")
print(database)

# Accessing a non-existing key with get() which avoids an exception
print("\nAccessing a non-existing key with get():")
print(database.get('004', 'Not Found'))  # Returns 'Not Found' if key does not exist

# Deleting an entry
del database['002']  # Removes Bob from the database

# Checking existence of a key
print("\nCheck if '002' exists after deletion:")
print('002' in database)  # Returns False since '002' has been deleted

# Iterating over items
print("\nCurrent Database Entries:")
for student_id, info in database.items():
    print(f"Student ID: {student_id}, Info: {info}")

# Dictionary methods like keys(), values(), and items()
print("\nDictionary Keys:")
print(database.keys())  # Prints all the keys in the dictionary

print("\nDictionary Values:")
print(database.values())  # Prints all the values in the dictionary

