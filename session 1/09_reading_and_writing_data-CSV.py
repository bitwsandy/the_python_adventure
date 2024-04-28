# Funny Python Script: The CSV Comedy Show

import csv

print("Welcome to The CSV Comedy Show!")
print("Get ready to laugh your way through some CSV file reading and writing!\n")

# Step 1: Open the CSV file
print("Step 1: Open the CSV file")
print("Now, let's see what's inside that mysterious CSV file...\n")

# Step 2: Read and Display the Data
print("Step 2: Read and Display the Data")

# Read the jokes from the CSV file
jokes = []
try:
    with open(r"C:\Users\Sandeep\Desktop\data\transactions\cr_all.txt", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            jokes.append(row)
            print(row[0], ",", row[1], ",", row[2])  # Display question and answer and ratings
    print("\nWow, what a hilarious collection of data!\n")
except FileNotFoundError:
    print("Oops! Can't find the CSV file. Looks like it's playing hide and seek!\n")

# Step 3: Write the Jokes to a New CSV File
print("Step 3: Write the Jokes to a New CSV File")

try:
    with open("../data_armory/outupts/laughter_killer.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(jokes)
    print("Hooray! The jokes have been successfully copied to a new CSV file.")
except Exception as e:
    print("Oops! Something went wrong while writing the CSV file:", e)
#
print("\nThat's the end of The CSV Comedy Show!")
print("Hope you enjoyed the performance. Until next time, keep laughing!")
