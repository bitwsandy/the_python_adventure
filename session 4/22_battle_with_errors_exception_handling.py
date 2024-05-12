# Exercise 1: Division by Zero Handling
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Please enter valid numbers.")


# Exercise 2: File Handling with Error Checking
try:
    filename = input("Enter the filename: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")


# Exercise 3: Input Validation with try-except
while True:
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
        break  # Exit loop if input is valid
    except ValueError:
        print("Error: Please enter a valid integer.")


# Exercise 4: Dictionary Key Error Handling
my_dict = {'a': 1, 'b': 2, 'c': 3}
try:
    key = input("Enter a key: ")
    value = my_dict[key]
    print("Value corresponding to key", key, "is:", value)
except KeyError:
    print("Error: Key not found in the dictionary.")