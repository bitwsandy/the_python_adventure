# main.py

from modules import math_operations_module
from modules.string_ops import string_operations_module

def main():
    try:
        # Test math_operations module
        print("Math Operations:")
        print("Division:", math_operations_module.divide(10, 2))
        print("Division:", math_operations_module.divide(10, 0))  # Raises ValueError

        # Test string_operations module
        # print("\nString Operations:")
        # print("Concatenation:", string_operations_module.concatenate_strings("Hello", "World"))
        # print("Concatenation:", string_operations_module.concatenate_strings("Hello", 123))  # Raises ValueError
    except ValueError as e:
        print("Error from main :", e)
    except Exception as e:
        print(f"Unknown Error Occured : {e}")

if __name__ == "__main__":
    main()