# Age Odyssey: Students embark on an epic journey through the ages,
# discovering their place in the world by unraveling the age-old mysteries of classification.

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
