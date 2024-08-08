import datetime

def date_operations_example():
    # Get the current date
    current_date = datetime.date.today()
    print("Current date:", current_date)

    # Create a specific date
    specific_date = datetime.date(2023, 10, 15)
    print("Specific date:", specific_date)

    # Get the year, month, and day of a date
    print("Year:", specific_date.year)
    print("Month:", specific_date.month)
    print("Day:", specific_date.day)

    # Format a date as a string
    formatted_date = specific_date.strftime("%Y-%m-%d")
    print("Formatted date:", formatted_date)

    # Parse a string to create a date
    parsed_date = datetime.datetime.strptime("2024-05-10", "%Y-%m-%d").date()
    print("Parsed date:", parsed_date)

    # Calculate the difference between two dates
    date1 = datetime.date(2022, 5, 10)
    date2 = datetime.date(2024, 5, 10)
    date_difference = date2 - date1
    print("Difference between dates:", date_difference.days, "days")

    # Add or subtract days from a date
    new_date = specific_date + datetime.timedelta(days=30)
    print("New date after adding 30 days:", new_date)

    # Compare two dates
    date3 = datetime.date(2024, 10, 15)
    if specific_date == date3:
        print("The dates are equal")
    elif specific_date < date3:
        print("Specific date is before date3")
    else:
        print("Specific date is after date3")

def datetime_operations_example():
    # Get the current datetime
    current_datetime = datetime.datetime.now()
    print("\nCurrent datetime:", current_datetime)

    # Create a specific datetime
    specific_datetime = datetime.datetime(2023, 10, 15, 12, 30, 45)
    print("Specific datetime:", specific_datetime)

    # Get the year, month, day, hour, minute, and second of a datetime
    print("Year:", specific_datetime.year)
    print("Month:", specific_datetime.month)
    print("Day:", specific_datetime.day)
    print("Hour:", specific_datetime.hour)
    print("Minute:", specific_datetime.minute)
    print("Second:", specific_datetime.second)

    # Format a datetime as a string
    formatted_datetime = specific_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted datetime:", formatted_datetime)

    # Parse a string to create a datetime
    parsed_datetime = datetime.datetime.strptime("2024-05-10 08:30:00", "%Y-%m-%d %H:%M:%S")
    print("Parsed datetime:", parsed_datetime)

    # Calculate the difference between two datetimes
    datetime1 = datetime.datetime(2022, 5, 10, 8, 0, 0)
    datetime2 = datetime.datetime(2024, 5, 10, 10, 30, 0)
    datetime_difference = datetime2 - datetime1
    print("Difference between datetimes:", datetime_difference)

    # Add or subtract time from a datetime
    new_datetime = specific_datetime + datetime.timedelta(hours=3, minutes=15)
    print("New datetime after adding 3 hours and 15 minutes:", new_datetime)

    # Compare two datetimes
    datetime3 = datetime.datetime(2024, 10, 15, 12, 30, 45)
    if specific_datetime == datetime3:
        print("The datetimes are equal")
    elif specific_datetime < datetime3:
        print("Specific datetime is before datetime3")
    else:
        print("Specific datetime is after datetime3")

if __name__ == "__main__":
    date_operations_example()
    datetime_operations_example()
