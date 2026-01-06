# Square of a Number:
#    Write a lambda function that takes a number as input and returns its square.

# Define a lambda function that takes 'x' as input and returns 'x' squared
square = lambda x: x**2
# Test the lambda function
print(square(5))  # Output: 25

# Study Drills :
# Create a lambda function which calculates square root of given number
# Create a lambda function which adds number to itself


# Addition of Two Numbers:
#    Write a lambda function that takes two numbers as input and returns their sum.
# Define a lambda function that takes 'x' and 'y' as input and returns their sum
addition = lambda x, y: x + y
# Test the lambda function
print(addition(3, 5))  # Output: 8


# Check Even Number:
#    Write a lambda function that takes a number as input and returns True if it's even,
#    otherwise False.
# Define a lambda function that takes 'x' as input and returns True if 'x' is even, else False
is_even = lambda x: x % 2 == 0
# Test the lambda function
print(is_even(6))  # Output: True
print(is_even(5))  # Output: False


# Reverse a String:
#    Write a lambda function that takes a string as input and returns the reversed
#    string.
# Define a lambda function that takes 's' as input and returns 's' reversed
reverse_string = lambda s: s[::-1]
# Test the lambda function
print(reverse_string("hello"))  # Output: "olleh"



# Sort List of Tuples by Second Element:
#    Write a lambda function to sort a list of tuples based on the second element of
#    each tuple.
# Define a list of tuples
data = [('John', 25), ('Doe', 30), ('Jane', 20)]
# Sort the list of tuples based on the second element using a lambda function
sorted_data = sorted(data, key=lambda x: x[1])
# Print the sorted list
print(sorted_data)  # Output: [('Jane', 20), ('John', 25), ('Doe', 30)]




# Sort List of Dictionaries by a Key:
#    Given a list of dictionaries, sort the list based on a specific key in each
#    dictionary.
# List of dictionaries
data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}, {'name': 'Doe', 'age': 35}]
# Sort the list of dictionaries based on the 'age' key using a lambda function
sorted_data = sorted(data, key=lambda x: x['age'])
# Print the sorted list
print(sorted_data)



# Filter List of Numbers:
#    Given a list of numbers, filter out the numbers that are divisible by 3.
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter the list of numbers to include only those divisible by 3 using a lambda function
filtered_numbers = list(filter(lambda x: x % 3 == 0, numbers))
# Print the filtered list
print(filtered_numbers)



# Calculate Factorials of Numbers:
#    Given a list of numbers, calculate the factorial of each number.
# List of numbers
numbers = [1,2 ,2, 3, 4, 5]
# Calculate the factorial of each number using a lambda function
factorials = list(map(lambda x: 1 if x == 0 else x * factorials(x - 1), numbers))
# Print the list of factorials
print(factorials)



# Find Maximum Value in List of Tuples:
#    Given a list of tuples, find the tuple with the maximum value based on a
#    specific element in each tuple.
# List of tuples
data = [('John', 30), ('Jane', 25), ('Doe', 35)]
# Find the tuple with the maximum age using a lambda function
max_tuple = max(data, key=lambda x: x[1])
# Print the tuple with the maximum age
print(max_tuple)



# Group List of Words by Length:
#    Given a list of words, group the words based on their lengths into a dictionary.
# List of words
words = ['apple', 'banana', 'orange', 'pear', 'kiwi']
# Group the words by length using a lambda function
grouped_words = {}
for word in words:
    length = len(word)
    grouped_words.setdefault(length, []).append(word)
# Print the grouped words
print(grouped_words)



"""
=========================================================
Lambda with map(), filter(), sorted() – Practical Exercises
Focus: Clean usage of lambda where it actually makes sense
=========================================================
"""

# =========================================================
# SECTION 1: map() + lambda (Transformation)
# =========================================================

# 1) Convert temperatures from Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("\n1) Celsius to Fahrenheit:", fahrenheit)


# 2) Clean city names (strip + title case)
cities = ["  mumbai ", "DELHI", " puNe "]
cleaned_cities = list(map(lambda c: c.strip().title(), cities))
print("2) Cleaned Cities:", cleaned_cities)


# 3) Derive total amount = qty * price
orders = [{"qty": 2, "price": 100}, {"qty": 1, "price": 250}, {"qty": 5, "price": 20}]
amounts = list(map(lambda o: o["qty"] * o["price"], orders))
print("3) Order Amounts:", amounts)


# =========================================================
# SECTION 2: filter() + lambda (Selection)
# =========================================================

# 4) Keep only even numbers
nums = [10, 15, 22, 7, 8]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("\n4) Even Numbers:", even_nums)


# 5) Filter valid emails (basic check)
emails = ["a@gmail.com", "bademail", "x@y", "test@company.in"]
valid_emails = list(filter(lambda e: "@" in e and "." in e.split("@")[-1], emails))
print("5) Valid Emails:", valid_emails)


# 6) Filter positive transaction amounts
transactions = [-100, 250, 0, -50, 400]
positive_txns = list(filter(lambda x: x > 0, transactions))
print("6) Positive Transactions:", positive_txns)


# =========================================================
# SECTION 3: sorted() + lambda (Ordering)
# =========================================================

# 7) Sort numbers in descending order
nums2 = [5, 2, 9, 1]
sorted_desc = sorted(nums2, key=lambda x: -x)
print("\n7) Sorted Desc:", sorted_desc)


# 8) Sort employees by salary
employees = [("Amit", 50000), ("Neha", 75000), ("Rahul", 60000)]
sorted_by_salary = sorted(employees, key=lambda x: x[1])
print("8) Sorted by Salary:", sorted_by_salary)


# 9) Sort orders by status then amount descending
orders2 = [
    {"order_id": "o1", "status": "COMPLETE", "amount": 200},
    {"order_id": "o2", "status": "PENDING", "amount": 500},
    {"order_id": "o3", "status": "PENDING", "amount": 120},
]

sorted_orders = sorted(orders2, key=lambda o: (o["status"], -o["amount"]))
print("9) Sorted Orders:", sorted_orders)


# =========================================================
# SECTION 4: map + filter + sorted (Mini Pipeline)
# =========================================================

# 10) Clean → filter → sort product prices
prices = [" 100 ", " -20", "abc", "50", " 200 "]

cleaned = map(lambda p: p.strip(), prices)
valid_nums = filter(lambda p: p.lstrip("-").isdigit(), cleaned)
ints = map(lambda p: int(p), valid_nums)
positive_sorted = sorted(filter(lambda x: x > 0, ints))

print("\n10) Final Clean Prices:", positive_sorted)





"""
=========================================================
Python Built-in Functions with lambda (SIMPLE DEMOS)
Functions covered (excluding map/filter/sorted):

min, max, sum, any, all, zip, enumerate, set, dict,
reduce, groupby, heapq

Goal:
Understand EACH function in isolation.
(No combinations yet – those come later.)
=========================================================
"""

from functools import reduce
from itertools import groupby
import heapq


# =========================================================
# 1) min() with lambda
# =========================================================
# Finds the smallest element based on a rule (key)

nums = [10, 5, 30, 2]
smallest = min(nums, key=lambda x: x)
print("\n1) min() :", smallest)   # 2


# =========================================================
# 2) max() with lambda
# =========================================================
# Finds the largest element based on a rule (key)

largest = max(nums, key=lambda x: x)
print("2) max() :", largest)      # 30


# =========================================================
# 3) sum() with lambda (via map idea, but simple)
# =========================================================
# Adds values after applying transformation

values = [100, 200, 50]
total = sum(lambda x: x for x in values)  # generator expression style
print("\n3) sum() :", total)              # 350


# =========================================================
# 4) any() with lambda
# =========================================================
# Returns True if ANY condition is True

nums2 = [10, -5, 20]
has_negative = any(lambda x: x < 0 for x in nums2)
print("\n4) any() :", has_negative)        # True


# =========================================================
# 5) all() with lambda
# =========================================================
# Returns True only if ALL conditions are True

all_positive = all(lambda x: x > 0 for x in nums2)
print("5) all() :", all_positive)          # False


# =========================================================
# 6) zip() with lambda
# =========================================================
# Pairs elements from two lists

qty = [2, 1, 5]
price = [100, 250, 20]

paired = list(zip(qty, price))
print("\n6) zip() :", paired)              # [(2,100),(1,250),(5,20)]

# Using lambda to compute one value from each pair
amounts = [ (lambda x: x[0] * x[1])(p) for p in paired ]
print("   zip + lambda :", amounts)        # [200,250,100]


# =========================================================
# 7) enumerate() with lambda
# =========================================================
# Adds index to each element

names = ["Amit", "Neha", "Rahul"]
indexed = [ (lambda x: (x[0], x[1]))(e) for e in enumerate(names) ]
print("\n7) enumerate() :", indexed)       # [(0,'Amit'),(1,'Neha'),(2,'Rahul')]


# =========================================================
# 8) set() with lambda
# =========================================================
# Removes duplicates after transformation

cities = ["Pune", " pune ", "PUNE"]
unique_cities = set((lambda c: c.strip().lower())(c) for c in cities)
print("\n8) set() :", unique_cities)       # {'pune'}


# =========================================================
# 9) dict() with lambda
# =========================================================
# Create key-value pairs dynamically

nums3 = [1, 2, 3]
squares = dict((lambda x: (x, x*x))(n) for n in nums3)
print("\n9) dict() :", squares)            # {1:1, 2:4, 3:9}


# =========================================================
# 10) reduce() with lambda
# =========================================================
# Combines values into a single result step-by-step

nums4 = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums4)
print("\n10) reduce() :", result)           # 10


# =========================================================
# 11) groupby() with lambda
# =========================================================
# Groups consecutive elements (DATA MUST BE SORTED FIRST)

data = [
    {"city": "Pune"},
    {"city": "Mumbai"},
    {"city": "Pune"},
]

# Sort first by city
data_sorted = sorted(data, key=lambda x: x["city"])

print("\n11) groupby() :")
for city, group in groupby(data_sorted, key=lambda x: x["city"]):
    print("   ", city, list(group))


# =========================================================
# 12) heapq (Top-N) with lambda
# =========================================================
# Efficient way to get largest/smallest elements

scores = [50, 10, 90, 30]
top2 = heapq.nlargest(2, scores, key=lambda x: x)
bottom2 = heapq.nsmallest(2, scores, key=lambda x: x)

print("\n12) heapq nlargest :", top2)       # [90,50]
print("    heapq nsmallest:", bottom2)      # [10,30]





"""
=========================================================
Gradual Combination: lambda + map/filter/sorted + others
For first-time learners (step-by-step building blocks)

How to teach:
Step 1: map only
Step 2: filter only
Step 3: sorted only
Step 4: map + filter
Step 5: filter + sorted
Step 6: map + sorted
Step 7: map + filter + sorted (pipeline)
Step 8: add other built-ins gradually (min/max/sum/any/all/zip/etc.)
=========================================================
"""

from functools import reduce
from itertools import groupby
import heapq


# ---------------------------------------------------------
# Sample data (simple but realistic)
# ---------------------------------------------------------
employees = [
    {"id": 1, "name": "Amit",  "salary": 50000, "city": " Pune ",   "email": "amit@gmail.com"},
    {"id": 2, "name": "Neha",  "salary": 75000, "city": "MUMBAI",   "email": "neha@company.in"},
    {"id": 3, "name": "Rahul", "salary": 60000, "city": "delhi  ",  "email": "bademail"},
    {"id": 4, "name": "Pooja", "salary": 90000, "city": " pune",    "email": "pooja@gmail.com"},
]


# A small helper lambda (kept simple & reusable)
clean_city = lambda c: c.strip().title()
is_valid_email_basic = lambda e: ("@" in e) and ("." in e.split("@")[-1])


# =========================================================
# STEP 1) map() only (Transform)
# =========================================================
# map applies a function to every element and returns an iterator
cities_cleaned = list(map(lambda e: clean_city(e["city"]), employees))
print("\nSTEP 1 - map() only - cleaned cities:", cities_cleaned)


# =========================================================
# STEP 2) filter() only (Select)
# =========================================================
valid_email_emps = list(filter(lambda e: is_valid_email_basic(e["email"]), employees))
print("\nSTEP 2 - filter() only - valid email employees:", [e["name"] for e in valid_email_emps])


# =========================================================
# STEP 3) sorted() only (Order)
# =========================================================
sorted_by_salary_desc = sorted(employees, key=lambda e: -e["salary"])
print("\nSTEP 3 - sorted() only - salary desc:", [(e["name"], e["salary"]) for e in sorted_by_salary_desc])


# =========================================================
# STEP 4) map + filter  (Transform after selection)
# =========================================================
# First filter valid emails, then map to names
valid_names = list(map(lambda e: e["name"],
                       filter(lambda e: is_valid_email_basic(e["email"]), employees)))
print("\nSTEP 4 - map + filter - names with valid emails:", valid_names)


# =========================================================
# STEP 5) filter + sorted  (Select, then order)
# =========================================================
# Filter employees with salary >= 60000, then sort by salary
filtered_then_sorted = sorted(
    filter(lambda e: e["salary"] >= 60000, employees),
    key=lambda e: e["salary"]
)
print("\nSTEP 5 - filter + sorted - salary>=60000 sorted asc:",
      [(e["name"], e["salary"]) for e in filtered_then_sorted])


# =========================================================
# STEP 6) map + sorted (Transform then order by transformed key)
# =========================================================
# Make a lightweight view (name, cleaned_city, salary) and then sort by city
view = list(map(lambda e: (e["name"], clean_city(e["city"]), e["salary"]), employees))
view_sorted_by_city = sorted(view, key=lambda x: x[1])

print("\nSTEP 6 - map + sorted - view sorted by city:")
print(view_sorted_by_city)


# =========================================================
# STEP 7) map + filter + sorted (Mini pipeline)
# =========================================================
# Pipeline goal:
# 1) Keep valid email employees
# 2) Create a clean output dict
# 3) Sort by salary descending

pipeline = sorted(
    map(
        lambda e: {"name": e["name"], "city": clean_city(e["city"]), "salary": e["salary"]},
        filter(lambda e: is_valid_email_basic(e["email"]), employees)
    ),
    key=lambda e: -e["salary"]
)

print("\nSTEP 7 - map + filter + sorted - pipeline output:")
print(pipeline)


# =========================================================
# STEP 8) Add OTHER built-ins on top of the pipeline
# (This is how real projects compute metrics/checks)
# =========================================================

# 8A) min/max from pipeline
highest = max(pipeline, key=lambda e: e["salary"])
lowest = min(pipeline, key=lambda e: e["salary"])
print("\nSTEP 8A - max/min on pipeline:", "highest =", highest, "| lowest =", lowest)

# 8B) sum of salaries in pipeline
total_salary = sum(map(lambda e: e["salary"], pipeline))
print("STEP 8B - sum salaries in pipeline:", total_salary)

# 8C) any/all checks (data quality style)
any_city_mumbai = any(map(lambda e: e["city"] == "Mumbai", pipeline))
all_salary_positive = all(map(lambda e: e["salary"] > 0, pipeline))
print("STEP 8C - any/all checks:", "any Mumbai? =", any_city_mumbai, "| all salary positive? =", all_salary_positive)

# 8D) set of cities (dedup)
unique_cities = set(map(lambda e: e["city"], pipeline))
print("STEP 8D - unique cities in pipeline:", unique_cities)

# 8E) dict mapping: name -> salary
name_to_salary = dict(map(lambda e: (e["name"], e["salary"]), pipeline))
print("STEP 8E - dict mapping name->salary:", name_to_salary)

# 8F) zip example (parallel lists) using lambda
names = list(map(lambda e: e["name"], pipeline))
salaries = list(map(lambda e: e["salary"], pipeline))
paired = list(zip(names, salaries))
print("STEP 8F - zip(names, salaries):", paired)

# 8G) enumerate for ranking (rank, name, salary)
ranked = list(map(lambda x: (x[0] + 1, x[1]["name"], x[1]["salary"]), enumerate(pipeline)))
print("STEP 8G - enumerate ranking:", ranked)

# 8H) reduce example (sum via reduce - demo)
salary_sum_reduce = reduce(lambda a, b: a + b, salaries, 0)
print("STEP 8H - reduce sum salaries (demo):", salary_sum_reduce)

# 8I) groupby (group by city) - requires sorting by city first
pipeline_sorted_by_city = sorted(pipeline, key=lambda e: e["city"])
print("\nSTEP 8I - groupby city:")
for city, grp in groupby(pipeline_sorted_by_city, key=lambda e: e["city"]):
    grp_list = list(grp)
    print(" ", city, "->", grp_list)

# 8J) heapq top-N
top1 = heapq.nlargest(1, pipeline, key=lambda e: e["salary"])
print("\nSTEP 8J - heapq top1 salary:", top1)







