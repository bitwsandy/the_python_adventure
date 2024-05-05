# Function with no parameters
def greet():
    """Prints a simple greeting message."""
    print("Hello, welcome!")

# Function with one parameter
def greet_name(name):
    """Greets the person with the given name."""
    print("Hello,", name, "!")

# Function with two parameters
def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# Function with three parameters
def calculate_area(length, width, height):
    """Calculates the area of a rectangular prism."""
    return 2 * (length * width + length * height + width * height)

# Function with default parameter
def greet_default(name="Guest"):
    """Greets the person with the given name or 'Guest' if no name is provided."""
    print("Hello,", name, "!")

# Call the functions
greet()
greet_name("Alice")
print("Sum:", add_numbers(3, 4))
print("Area:", calculate_area(2, 3, 4))
greet_default()  # Using default value
greet_default("Bob")  # Providing a custom value


# 1. Function Definition :
#       Functions are defined using the `def` keyword followed by the function name
#       and parentheses containing parameters (if any). For example:

        # def greet():
        #     print("Hello, welcome!")
        # Here, `greet` is the function name, and it takes no parameters.

# 2. Function Parameters:
#       Parameters are variables that hold the values passed to the function when it is called.
#       For example:

       # def greet_name(name):
       #     print("Hello,", name, "!")
       # Here, `name` is a parameter of the `greet_name` function.

# 3. Function Call :
#      Functions are executed by calling them with parentheses containing arguments (if required). For example:

       # greet_name("Alice")
       # This calls the `greet_name` function with the argument `"Alice"`.

# 4. Return Statement :
#       The `return` statement exits the function and returns a
#       value (if specified) to the caller. For example:

       # def add_numbers(a, b):
       #     return a + b
       # Here, the `add_numbers` function returns the sum of `a` and `b`.

# 5. Default Parameters :
#       Functions can have default parameter values,
#       which are used if no argument is provided when the function is called. For example:

       # def greet_default(name="Guest"):
       #     print("Hello,", name, "!")
       #
       # Here, `name` has a default value of `"Guest"`.

# 6. Docstrings : Docstrings are optional documentation strings that describe
#       the purpose and usage of a function. They are placed inside triple quotes immediately after the function definition. For example:

       # def greet():
       #     """Prints a simple greeting message."""
       #     print("Hello, welcome!")
       #
       # Here, `"""Prints a simple greeting message."""` is the docstring for the `greet` function.

