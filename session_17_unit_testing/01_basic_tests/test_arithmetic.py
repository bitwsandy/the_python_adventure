# test_arithmetic.py
# --------------------------------------------------------------
# Unittest demo for arithmetic.py
# Shows:
# - creating a test module & test class
# - multiple tests (including parameterized via subTest)
# - success + one intentional failure (to show red output)
# - division vs floor division edge cases
# - assertRaises as a context manager
# - running via `python -m unittest` OR `python test_arithmetic.py`
# --------------------------------------------------------------

import unittest
import arithmetic  # module under test


class TestArithmeticBasics(unittest.TestCase):
    """Basic passing tests for add/sub/mul."""

    def test_add(self):
        self.assertEqual(arithmetic.add(2, 3), 5)
        self.assertEqual(arithmetic.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(arithmetic.sub(10, 4), 6)
        self.assertEqual(arithmetic.sub(-2, -3), 1)

    def test_mul(self):
        self.assertEqual(arithmetic.mul(3, 4), 12)
        self.assertEqual(arithmetic.mul(-2, 5), -10)


# -------------------------------------------------------------
# Multiple test cases for the same function using subTest
# -------------------------------------------------------------
class TestMultipleCasesWithSubTest(unittest.TestCase):
    """Demonstrate multiple tests for a single function using subTest.
       subTest lets us run several mini-tests inside one test method.
       If one case fails, the others still continue.
    """

    def test_add_many(self):
        # Each tuple in this list represents one test case
        # Format: (a, b, expected_result)
        cases = [
            (0, 0, 0),     # simple zero addition
            (1, 2, 3),     # normal positive numbers
            (-1, -2, -3),  # both negative
            (-5, 10, 5),   # mix of negative and positive
        ]

        # Loop through all test cases
        for a, b, expected in cases:
            # subTest creates an independent sub-test for each case.
            # This prevents the loop from stopping if one test fails.
            with self.subTest(a=a, b=b):
                # Compare the function output to the expected result
                self.assertEqual(arithmetic.add(a, b), expected)


# -------------------------------------------------------------
#  Division-related tests (normal and edge cases)
# -------------------------------------------------------------
class TestDivision(unittest.TestCase):
    """Focus on true division vs floor division + error handling."""

    def test_true_division(self):
        # True division `/` preserves fractions (float results)
        self.assertEqual(arithmetic.div(5, 2), 2.5)

        # assertAlmostEqual → used for floating-point comparisons
        # "places=7" means it checks equality up to 7 decimal places
        self.assertAlmostEqual(arithmetic.div(1, 3), 0.3333333333, places=7)

    def test_floor_division_positive(self):
        # Floor division `//` drops the decimal part and rounds down
        self.assertEqual(arithmetic.floordiv(5, 2), 2)  # 2.5 → 2
        self.assertEqual(arithmetic.floordiv(9, 3), 3)  # 9/3 = 3.0 → 3

    def test_floor_division_negative(self):
        # Important edge case:
        # When either number is negative, floor division rounds toward -infinity
        # Example: -5 // 2 = -3  (not -2)
        # Example:  5 // -2 = -3  (not -2)
        self.assertEqual(arithmetic.floordiv(-5, 2), -3)
        self.assertEqual(arithmetic.floordiv(5, -2), -3)

    def test_zero_division_errors(self):
        """Demonstrates assertRaises to test exceptions."""
        # assertRaises checks that an operation raises an expected error.
        # It is used as a context manager (with ... : block)
        with self.assertRaises(ZeroDivisionError):
            arithmetic.div(1, 0)

        with self.assertRaises(ZeroDivisionError):
            arithmetic.floordiv(1, 0)

        with self.assertRaises(ZeroDivisionError):
            arithmetic.mod(1, 0)


# -------------------------------------------------------------
#  Demonstrate a failing test on purpose
# -------------------------------------------------------------
@unittest.expectedFailure
class TestIntentionalFailureDemo(unittest.TestCase):
    """This test intentionally fails to demonstrate red output and failure reports.

    Tip: Keep an 'expected failure' test to show how failures look.
    After the demo, mark it as @unittest.expectedFailure to keep the suite green.
    """

    def test_intentional_failure(self):
        # WRONG ON PURPOSE: 2 + 2 is not 5
        # This shows what a failure looks like in test output.
        # Run once → you'll see FAIL (AssertionError)
        # Then you can fix or mark as expectedFailure.
        self.assertEqual(arithmetic.add(2, 2), 5)


# -------------------------------------------------------------
#  Demonstrate expectedFailure decorator
# -------------------------------------------------------------
@unittest.expectedFailure
class TestExpectedFailurePattern(unittest.TestCase):
    """The @expectedFailure decorator marks tests that are *known* to fail.

    When these tests fail, unittest marks them as 'expected failure'
    instead of turning the entire run red.
    """

    def test_known_bug_example(self):
        # Pretend this test is for a known bug not yet fixed.
        # If this assertion fails, it won't mark the suite as FAILED.
        self.assertEqual(arithmetic.sub(2, 2), 1)


# -------------------------------------------------------------
# Run the tests
# -------------------------------------------------------------
if __name__ == "__main__":
    # unittest.main() discovers and runs all tests in this file.
    # verbosity=2 → shows detailed output with test names and status.
    unittest.main(verbosity=2)

"""
-------------------------------------------------------------
RUNNING THE TESTS (from command line)
-------------------------------------------------------------

Option 1: Run this file directly
    python test_arithmetic.py
    python test_arithmetic.py -v    # verbose output

Option 2: Run using unittest discovery
    python -m unittest
    python -m unittest -v

Option 3: Run only one specific class or method
    python -m unittest test_arithmetic.TestDivision
    python -m unittest test_arithmetic.TestDivision.test_true_division

-------------------------------------------------------------
WHAT YOU'LL SEE IN OUTPUT
-------------------------------------------------------------
✔ PASSED tests → 'ok'
✖ FAILED tests → 'FAIL' (with traceback)
⚠ EXPECTED failures → 'expected failure' or 'xfailed'
-------------------------------------------------------------
"""

