file_name = r"C:\Users\Sandeep\Desktop\data\wordcount.txt"


import csv

input_file = r"C:\Users\Sandeep\Desktop\data\cr.txt"
output_file = r"C:\Users\Sandeep\Desktop\data\cr_op.txt"

# Read data from the input CSV file
with open(input_file, "r", newline='') as infile:
    reader = csv.reader(infile)
    data = list(reader)

print(data)

# Perform operations on the data (e.g., calculate total of a column)
total_rows = len(data)
total_columns = len(data[0])
#
# Write the results to a new CSV file
with open(output_file, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Total"])
    writer.writerow([total_rows])
    writer.writerow([total_columns])

print("Results written to output.csv")


