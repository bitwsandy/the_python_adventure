# Funny Python Script: The Excel Comedy Show

# Dependencies :
#     1. Openpyxl
#     2. pandas

import pandas as pd

print("Welcome to The Excel Comedy Show!")
print("Get ready to laugh your way through some Excel file reading and writing!\n")

# Step 1: Open the Excel file
print("Step 1: Open the Excel file")
print("Now, let's see what's inside that mysterious Excel file...\n")

# Step 2: Read and Display the Data
print("Step 2: Read and Display the Data")

# Read the jokes from the Excel file
try:
    df = pd.read_excel("../data_armory/funny_jokes.xlsx")
    print(df)
    print("\nWow, what a hilarious collection of data!\n")
except FileNotFoundError:
    print("Oops! Can't find the Excel file. Looks like it's playing hide and seek!\n")

# Step 3: Write the Jokes to a New Excel File
print("Step 3: Write the Jokes to a New Excel File")

try:
    df.to_excel(r"C:\Users\Sandeep\PycharmProjects\python_hands_on\data_armory\outupts\funny_jokes_copy.xlsx", index=False)
    print("Hooray! The jokes have been successfully copied to a new Excel file.")
except Exception as e:
    print("Oops! Something went wrong while writing the Excel file:", e)

print("\nThat's the end of The Excel Comedy Show!")
print("Hope you enjoyed the performance. Until next time, keep laughing!")
