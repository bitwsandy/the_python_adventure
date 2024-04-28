# Leap Year Quest: Students embark on a journey through time,
# unraveling the secrets of leap years to ensure the accuracy of their temporal calculations.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
