# Leap Year Quest: Students embark on a journey through time,
# unraveling the secrets of leap years to ensure the accuracy of their temporal calculations.

year = int(input("Enter a year: "))
print(f"Type of Year : {type(year)}")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
# if all conditions are true then and only then and will return true
# if all conditions are flase the n and only then or will return false