# test_employee.py
# --------------------------------------------------------------
# UNIT TESTS for Employee
# --------------------------------------------------------------
# What this file demonstrates:
# 1) Creating a test MODULE and a test CLASS
# 2) Manual object construction vs. setUp/tearDown-managed objects
# 3) setUpClass / tearDownClass (class-wide fixtures) with print markers
# 4) Multiple tests and visible execution ORDER via print statements
# 5) Tests for fullname, email, apply_raise (including class-attr override)
# 6) Notes and scenarios embedded as comments for teaching
# --------------------------------------------------------------

import unittest
from employee import Employee

# --------------------------------------------------------------
# A. Manual creation tests (no setUp/tearDown)
# --------------------------------------------------------------
class TestEmployee_Manual(unittest.TestCase):
    """Manual construction per test (clear but repetitive).
    Use when each test needs bespoke setup different from others.
    """

    def test_fullname_manual(self):
        print("\n[TestEmployee_Manual.test_fullname_manual] running")
        emp = Employee("Sandeep", "Patil", 50000)
        self.assertEqual(emp.fullname(), "Sandeep Patil")

    def test_email_manual(self):
        print("\n[TestEmployee_Manual.test_email_manual] running")
        emp = Employee("Sandeep", "Patil", 50000)
        self.assertEqual(emp.email(), "sandeep.patil@company.com")

    def test_apply_raise_manual(self):
        print("\n[TestEmployee_Manual.test_apply_raise_manual] running")
        emp = Employee("Sandeep", "Patil", 50000)
        # Default class raise = 1.10 (10%)
        emp.apply_raise()
        self.assertEqual(emp.salary, 55000.0)


# --------------------------------------------------------------
# B. Using setUp / tearDown (per-test fixtures)
# --------------------------------------------------------------
class TestEmployee_WithSetup(unittest.TestCase):
    """Demonstrate setUp/tearDown (runs before/after EVERY test method).
    Use when many tests share similar objects/config.
    """
    #
    # @classmethod
    # def setUpClass(cls):
    #     # setUpClass runs ONCE before any tests in this class.
    #     # Good for expensive fixtures (DB connections, temp dirs, etc.)
    #     print("\n=== [TestEmployee_WithSetup.setUpClass] START CLASS FIXTURE ===")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # tearDownClass runs ONCE after all tests in this class.
    #     print("=== [TestEmployee_WithSetup.tearDownClass] END CLASS FIXTURE ===")
    #
    # def setUp(self):
    #     # setUp runs BEFORE EACH test method
    #     print(f"\n[setUp] preparing fresh employees for: {self.id()}")
    #     self.emp1 = Employee("Alice", "Smith", 60000)
    #     self.emp2 = Employee("Bob", "Brown", 45000)
    #
    # def tearDown(self):
    #     # tearDown runs AFTER EACH test method
    #     print(f"[tearDown] cleaning up after: {self.id()}")
    #     # If you had open files or patches, you would restore/close here.
    #     del self.emp1
    #     del self.emp2
    #
    # # ----- Tests below automatically get fresh emp1/emp2 each time -----
    #
    # def test_fullname_updates_when_names_change(self):
    #     print("[test_fullname_updates_when_names_change] running")
    #     self.assertEqual(self.emp1.fullname(), "Alice Smith")
    #     # Scenario: user updates name; fullname should reflect latest state
    #     self.emp1.firstname = "Alicia"
    #     self.emp1.lastname = "Smyth"
    #     self.assertEqual(self.emp1.fullname(), "Alicia Smyth")
    #
    # def test_email_reflects_current_names(self):
    #     print("[test_email_reflects_current_names] running")
    #     self.assertEqual(self.emp2.email(), "bob.brown@company.com")
    #     # Scenario: after marriage, last name changes → email() should reflect
    #     self.emp2.lastname = "Williams"
    #     self.assertEqual(self.emp2.email(), "bob.williams@company.com")
    #
    # def test_apply_raise_uses_class_attribute_and_is_overridable(self):
    #     print("[test_apply_raise_uses_class_attribute_and_is_overridable] running")
    #     # Save original to restore later (important in shared test environments)
    #     original_raise = Employee.salary_raise
    #     # Use addCleanup to guarantee restoration even if the test fails halfway
    #     self.addCleanup(lambda: setattr(Employee, "salary_raise", original_raise))
    #
    #     # Temporarily change the CLASS raise percentage for this test
    #     Employee.salary_raise = 1.20  # 20% raise for this scenario
    #     self.emp1.apply_raise()
    #     self.assertEqual(self.emp1.salary, 72000.0)  # 60000 * 1.20
    #
    #     # Another employee should also honor the updated class attribute
    #     self.emp2.apply_raise()
    #     self.assertEqual(self.emp2.salary, 54000.0)  # 45000 * 1.20


# --------------------------------------------------------------
# C. setUpClass/tearDownClass with multiple tests to see order
# --------------------------------------------------------------
# class TestEmployee_OrderAndVisibility(unittest.TestCase):
#     """This class exists to make execution order & prints obvious.
#     - setUpClass/tearDownClass wrap the entire class' run
#     - setUp/tearDown wrap each test
#     - Test methods run in alphabetical order by name by default
#       (CPython's unittest sorts test method names).
#     """
#
    @classmethod
    def setUpClass(cls):
        print("\n=== [TestEmployee_OrderAndVisibility.setUpClass] ===")

    @classmethod
    def tearDownClass(cls):
        print("=== [TestEmployee_OrderAndVisibility.tearDownClass] ===")

    def setUp(self):
        print(f"[setUp] ({self.__class__.__name__}) for {self._testMethodName}")
        self.emp = Employee("Test", "Order", 10000)

    def tearDown(self):
        print(f"[tearDown] ({self.__class__.__name__}) for {self._testMethodName}")
        del self.emp

    def test_a_fullname(self):
        print("[test_a_fullname] running")
        self.assertEqual(self.emp.fullname(), "Test Order")

    def test_b_email(self):
        print("[test_b_email] running")
        self.assertEqual(self.emp.email(), "test.order@company.com")

    def test_c_raise(self):
        print("[test_c_raise] running")
        # Restore-safe tweak of class attribute using addCleanup
        original = Employee.salary_raise
        self.addCleanup(lambda: setattr(Employee, "salary_raise", original))
        Employee.salary_raise = 1.50
        self.emp.apply_raise()
        self.assertEqual(self.emp.salary, 15000.0)


# --------------------------------------------------------------
# D. How to run (notes for learners)
# --------------------------------------------------------------
# - From project folder:
#     python -m unittest -v
# - Or run just this file:
#     python test_employee.py -v
# - Or a single class / method:
#     python -m unittest test_employee.TestEmployee_WithSetup
#     python -m unittest test_employee.TestEmployee_WithSetup.test_email_reflects_current_names
#
# SCENARIOS TO DISCUSS (for class):
# - Why keep business logic small & pure? → easy to test
# - Using setUp when many tests need similar objects
# - When to use setUpClass → expensive/rarely-changing fixtures
# - Temporarily changing class attributes for a scenario, then restoring
# - Ensuring tests remain isolated & order-independent
# --------------------------------------------------------------


if __name__ == "__main__":
    # Allow running this module directly via: python test_employee.py -v
    unittest.main(verbosity=2)
