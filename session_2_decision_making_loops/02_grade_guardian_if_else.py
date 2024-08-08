# Exercise 1: Grade Guardian :
# Students embark on a quest to uncover their academic destiny
# by deciphering their grades in the mystical realm of education.

# Write a Python program that takes a student's score as input
# and classifies it into different grades: A, B, C, D, or F,
# based on the following criteria:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

score = 98
# 71, 85, 67, 49, 35, 91 , 98

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")