# Funny Python Program: Data Type Exercises

# Exercise 1: Integer Fun
print("Exercise 1: Integer Fun")
my_age = 25
your_age = 30
age_diff = your_age - my_age
print("I am", my_age, "years old.")
print("You are", your_age, "years old.")
print("The age difference between us is", age_diff, "years.\n")

# Exercise 2: String Tricks
print("Exercise 2: String Tricks")
my_name = "Bob"
your_name = "Alice"
greeting = "Hello, {} and {}!".format(my_name, your_name)
print(greeting)
print("The length of my name is", len(my_name), "characters.")
print("The length of your name is", len(your_name), "characters.\n")



# Exercise 3: Floaty Business
print("Exercise 3: Floaty Business")
item_price = 9.99
quantity = 3
total_cost = item_price * quantity
print("The price of one item is $", item_price)
print("You bought", quantity, "items.")
print("Your total cost is $", total_cost, "\n")

# Exercise 4: Boolean Bonanza
print("Exercise 4: Boolean Bonanza")
likes_cheese = True
likes_chocolate = False
print("Do I like cheese?", likes_cheese)
print("Do I like chocolate?", likes_chocolate)

# Bonus Exercise: The Ultimate Decision Maker
print("\nBonus Exercise: The Ultimate Decision Maker")
print("Should you buy a pizza?")
hungry = True
has_money = True
decision = hungry and has_money # [True and False : False]
print("Am I hungry?", hungry)
print("Do I have money?", has_money)
print("Decision:", decision)
if decision:
    print("Go for it, treat yourself to a pizza!")
else:
    print("Maybe save your money for now.\n")
