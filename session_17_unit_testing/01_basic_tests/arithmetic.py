# arithmetic.py
# --------------------------------------------------------------
# Simple arithmetic functions we want to test.
# Keep logic tiny so the focus stays on testing techniques.
# --------------------------------------------------------------

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    """True division; raises ZeroDivisionError if b == 0."""
    return a / b

def floordiv(a, b):
    """Floor division; raises ZeroDivisionError if b == 0."""
    return a // b

def mod(a, b):
    """Remainder (modulus); raises ZeroDivisionError if b == 0."""
    return a % b
