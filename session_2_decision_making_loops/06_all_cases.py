"""
=====================================================
Python if / elif / else / nested if-else – Solutions
=====================================================
This script covers:
1. if – elif – else
2. Nested if-else
3. Validation logic
4. Real-world decision making
"""

# --------------------------------------------------
# EXERCISE 1: Number Classification
# --------------------------------------------------

num = int(input("Exercise 1 | Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


print("\n----------------------------------\n")


# --------------------------------------------------
# EXERCISE 2: Student Result Evaluation
# --------------------------------------------------

marks = int(input("Exercise 2 | Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


print("\n----------------------------------\n")


# --------------------------------------------------
# EXERCISE 3: Login Validation (Nested if-else)
# --------------------------------------------------

correct_username = "admin"
correct_password = "pass123"

username = input("Exercise 3 | Enter username: ")
password = input("Exercise 3 | Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


print("\n----------------------------------\n")


# --------------------------------------------------
# EXERCISE 4: Electricity Bill Calculator
# --------------------------------------------------

units = int(input("Exercise 4 | Enter units consumed: "))

if units < 0:
    print("Invalid input")
else:
    bill = 0

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)
    else:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    print("Total Bill: ₹", bill)


print("\n----------------------------------\n")


# --------------------------------------------------
# EXERCISE 5: Bank Withdrawal System
# --------------------------------------------------

balance = 10000
amount = int(input("Exercise 5 | Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    if amount % 100 != 0:
        print("Enter amount in multiples of 100")
    else:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
