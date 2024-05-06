# Funny Python Program: The Formatting Frenzy

print("Welcome to The Formatting Frenzy!")
print("Get ready to dive into the wild world of printing with style!\n")

# Step 1: Basic Printing
print("Step 1: Basic Printing")
print("Let's start with some basic printing. Here's a simple message:\n")
print("Hello, World!\n")

# Step 2: String Formatting
print("Step 2: String Formatting")
print("Now, let's add some formatting to our message.\n")

# Method 1: Using f-strings (Python 3.6+)
name = "Alice"
age = 30
height = 172
print(f"Hello, {name}! You are {age} years old.\n")

# Method 2: Using the format() method
print("Hey there, {}! How are you on this lovely day?".format(name))

# Method 3: Using % formatting (Older method)
print("Oh, {}! You're {}? I thought you were younger!".format(name,age))

print("\nWow, look at all these different ways to format strings! It's a formatting fiesta!\n")

# Step 3: Numeric Formatting
print("Step 3: Numeric Formatting")
print("Let's make some numbers look fancy!\n")

# Method 1: Using f-strings with numeric formatting
pi_value = 3.141592653589793
print(f"The value of pi is approximately {pi_value:.2f} (rounded to 2 decimal places).\n")

# Method 2: Using the format() method with numeric formatting
salary = 50000
print("I earn ${:,.2f} per year. Living the high life!\n".format(salary))

print("Formatting numbers is like dressing them up for a party! Looking sharp!\n")

print("That's the end of The Formatting Frenzy!")
print("Hope you enjoyed learning about formatting while printing. Stay stylish, my friend!")
