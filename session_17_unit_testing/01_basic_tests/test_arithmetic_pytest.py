# test_arithmetic_pytest_functions.py
# --------------------------------------------------------------
# Pytest version of arithmetic tests WITHOUT classes.
# Semantics match the unittest version:
# - Same test logic and scenarios
# - Multiple cases for add (like subTest → now parametrize)
# - True vs floor division
# - ZeroDivisionError checks
# - Intentional failing test (marked xfail)
# - Known bug test (marked xfail)
# --------------------------------------------------------------

import pytest
import arithmetic  # module under test


# --------------------------------------------------------------
# Basic passing tests for add/sub/mul
# --------------------------------------------------------------

def test_add_basic():
    assert arithmetic.add(2, 3) == 5
    assert arithmetic.add(-1, 1) == 0


def test_sub_basic():
    assert arithmetic.sub(10, 4) == 6
    assert arithmetic.sub(-2, -3) == 1


def test_mul_basic():
    assert arithmetic.mul(3, 4) == 12
    assert arithmetic.mul(-2, 5) == -10


# --------------------------------------------------------------
# Multiple test cases for add (pytest equivalent of subTest)
# --------------------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),      # simple zero addition
        (1, 2, 3),      # normal positive numbers
        (-1, -2, -3),   # both negative
        (-5, 10, 5),    # mix of negative and positive
    ],
)
def test_add_many(a, b, expected):
    # Each (a, b, expected) becomes a separate test case in pytest.
    assert arithmetic.add(a, b) == expected


# --------------------------------------------------------------
# Division-related tests (normal and edge cases)
# --------------------------------------------------------------

def test_true_division():
    # True division `/` preserves fractional parts
    assert arithmetic.div(5, 2) == 2.5

    # Use pytest.approx for floating-point comparison (like assertAlmostEqual)
    assert arithmetic.div(1, 3) == pytest.approx(0.3333333333, rel=1e-7)


def test_floor_division_positive():
    # Floor division `//` drops the decimal part and rounds down
    assert arithmetic.floordiv(5, 2) == 2   # 2.5 → 2
    assert arithmetic.floordiv(9, 3) == 3   # 9/3 = 3.0 → 3


def test_floor_division_negative():
    # Important edge case:
    # When either number is negative, floor division rounds toward -infinity
    # Example: -5 // 2 = -3  (not -2)
    # Example:  5 // -2 = -3 (not -2)
    assert arithmetic.floordiv(-5, 2) == -3
    assert arithmetic.floordiv(5, -2) == -3


def test_zero_division_errors():
    """Demonstrates pytest.raises to test exceptions (context manager)."""
    with pytest.raises(ZeroDivisionError):
        arithmetic.div(1, 0)

    with pytest.raises(ZeroDivisionError):
        arithmetic.floordiv(1, 0)

    with pytest.raises(ZeroDivisionError):
        arithmetic.mod(1, 0)


# --------------------------------------------------------------
# Intentional failing test → expected failure (xfail)
# --------------------------------------------------------------

@pytest.mark.xfail(
    reason="Intentional demo failure: 2 + 2 is not 5",
    strict=False,
)
def test_intentional_failure_demo():
    """This test is WRONG on purpose to demonstrate failure/xfail behavior."""
    assert arithmetic.add(2, 2) == 5


# --------------------------------------------------------------
# Known bug pattern → expected failure (xfail)
# --------------------------------------------------------------

@pytest.mark.xfail(
    reason="Known bug example: sub(2, 2) should not be 1",
    strict=False,
)
def test_known_bug_example():
    """Known-bug style test: failure is expected, does not turn suite red."""
    assert arithmetic.sub(2, 2) == 1


"""
-------------------------------------------------------------
RUNNING THESE TESTS WITH PYTEST
-------------------------------------------------------------

From the folder containing this file:

1) Run all tests:
    pytest
    pytest -v

2) Run only this file:
    pytest test_arithmetic_pytest_functions.py
    pytest test_arithmetic_pytest_functions.py -v

3) Run a single test function:
    pytest test_arithmetic_pytest_functions.py::test_true_division
    pytest test_arithmetic_pytest_functions.py::test_add_many

XFAIL behavior:
- xfailed tests (expected to fail) will show as "XFAIL"
- if they start passing, they become "XPASS" (unexpected pass)
-------------------------------------------------------------
"""
