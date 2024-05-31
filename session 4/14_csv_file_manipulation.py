# 3. CSV File Manipulation:
#    Write a Python program that reads data from a CSV file, performs some operations
# (e.g., calculating the total, average, or maximum value of a column), and
# then writes the results to a new CSV file.

import csv

input_file = "input.csv"
output_file = "output.csv"

# Read data from the input CSV file
with open(input_file, "r", newline='') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Perform operations on the data (e.g., calculate total of a column)
total_rows = len(data)
total_columns = len(data[0])

# Write the results to a new CSV file
with open(output_file, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Total"])
    writer.writerow([total_rows])
    writer.writerow([total_columns])

print("Results written to output.csv")


