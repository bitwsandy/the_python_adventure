import pandas as pd


# Set display option to show all columns
pd.set_option('display.max_columns', None)

# If you want to ensure that all rows are displayed as well, use:
# pd.set_option('display.max_rows', None)

# # Reset display options to default
# pd.reset_option('display.max_columns')
# # pd.reset_option('display.max_rows')  # To reset row display limit as well
#


# Task 1: Load the Excel file into a Pandas DataFrame
df = pd.read_excel('data/employee.xlsx')
# The above line reads the Excel file into a DataFrame.
# Make sure the file 'employee_data.xlsx' is in your working directory.

# Task 2: Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:\n", df.head())
# head() shows the first 5 rows by default.