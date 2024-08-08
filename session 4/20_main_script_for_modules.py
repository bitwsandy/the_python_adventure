# main.py
from modules.string_ops import string_operations_module
from modules import list_operations_module
from modules import math_operations_module

# Math operations
result_add = math_operations_module.add(5, 3)
result_subtract = math_operations_module.subtract(5, 3)
result_multiply = math_operations_module.multiply(5, 3)
result_divide = math_operations_module.divide(5, 3)

print("Math Operations:")
print("5 + 3 =", result_add)
print("5 - 3 =", result_subtract)
print("5 * 3 =", result_multiply)
print("5 / 3 =", result_divide)

# String operations
string = "hello world"
capitalized_string = string_operations_module.capitalize_string(string)
reversed_string = string_operations_module.reverse_string(string)
vowel_count = string_operations_module.count_vowels(string)

print("\nString Operations:")
print("Capitalized String:", capitalized_string)
print("Reversed String:", reversed_string)
print("Vowel Count:", vowel_count)

# List operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
max_number = list_operations_module.find_max(numbers)
min_number = list_operations_module.find_min(numbers)
sorted_numbers = list_operations_module.sort_list(numbers)
average_number = list_operations_module.average(numbers)

print("\nList Operations:")
print("Max Number:", max_number)
print("Min Number:", min_number)
print("Sorted Numbers:", sorted_numbers)
print("Average Number:", average_number)






# # main.py
# from modules.string_ops.string_operations_module import *
# from modules.list_operations_module import *
# from modules.math_operations_module import *
#
# # Math operations
# result_add = add(5, 3)
# result_subtract = subtract(5, 3)
# result_multiply = multiply(5, 3)
# result_divide = divide(5, 3)
#
# print("Math Operations:")
# print("5 + 3 =", result_add)
# print("5 - 3 =", result_subtract)
# print("5 * 3 =", result_multiply)
# print("5 / 3 =", result_divide)
#
# # String operations
# string = "hello world"
# capitalized_string = capitalize_string(string)
# reversed_string = reverse_string(string)
# vowel_count = count_vowels(string)
#
# print("\nString Operations:")
# print("Capitalized String:", capitalized_string)
# print("Reversed String:", reversed_string)
# print("Vowel Count:", vowel_count)
#
# # List operations
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# max_number = find_max(numbers)
# min_number = find_min(numbers)
# sorted_numbers = sort_list(numbers)
# average_number = average(numbers)
#
# print("\nList Operations:")
# print("Max Number:", max_number)
# print("Min Number:", min_number)
# print("Sorted Numbers:", sorted_numbers)
# print("Average Number:", average_number)

