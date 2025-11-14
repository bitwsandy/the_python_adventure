# test_employee_pytest_functions.py
# --------------------------------------------------------------
# Pytest version of Employee tests (NO unittest.TestCase, NO classes)
# Demonstrates:
# - Manual instance creation tests
# - pytest fixtures as equivalents of setUp / tearDown
# - "Class-level" setup/teardown using module-scoped fixtures
# - Multiple tests and visible execution order via print()
# - Overriding and restoring a class attribute (salary_raise)
# --------------------------------------------------------------

import pytest
from employee import Employee


# ==============================================================
# SECTION A: Simple tests with MANUAL instance creation
# ==============================================================

def test_fullname_manual():
    print("\n[test_fullname_manual] running")
    emp = Employee("Sandeep", "Patil", 50000)
    assert emp.fullname() == "Sandeep Patil"


def test_email_manual():
    print("\n[test_email_manual] running")
    emp = Employee("Sandeep", "Patil", 50000)
    assert emp.email() == "sandeep.patil@company.com"


def test_apply_raise_manual():
    print("\n[test_apply_raise_manual] running")
    emp = Employee("Sandeep", "Patil", 50000)
    # Default salary_raise = 1.10 (10%)
    emp.apply_raise()
    assert emp.salary == 55000.0


# ==============================================================
# SECTION B: Using pytest fixtures like setUp/tearDown
# ==============================================================

@pytest.fixture(scope="module")
def module_banner():
    """
    This fixture is similar in spirit to setUpClass/tearDownClass.

    - scope="module" → runs once for this test file.
    - Code before `yield` ≈ setUpClass
    - Code after `yield`  ≈ tearDownClass
    - autouse=True would make it apply to all tests in module automatically,
      but here we'll use it explicitly where needed.
    """
    print("\n=== [module_banner] MODULE SETUP (similar to setUpClass) ===")
    yield
    print("=== [module_banner] MODULE TEARDOWN (similar to tearDownClass) ===")


@pytest.fixture
def emp_pair():
    """
    This fixture acts like setUp/tearDown for each test needing emp1 and emp2.

    - Scope: function (default) → runs before each test that uses it.
    - Code before `yield` ≈ setUp
    - Code after  `yield` ≈ tearDown
    """
    print("[emp_pair] setUp-like: creating emp1 & emp2")
    emp1 = Employee("Alice", "Smith", 60000)
    emp2 = Employee("Bob", "Brown", 45000)
    # Provide employees to the test
    yield emp1, emp2
    # Teardown part
    print("[emp_pair] tearDown-like: cleaning up emp1 & emp2")
    del emp1
    del emp2


def test_fullname_updates_when_names_change(module_banner, emp_pair):
    """
    Uses:
    - module_banner → prints class-level style setup/teardown once for this file
    - emp_pair      → fresh emp1/emp2 for each test
    """
    print("[test_fullname_updates_when_names_change] running")
    emp1, _ = emp_pair

    # Initial fullname
    assert emp1.fullname() == "Alice Smith"

    # Scenario: name updated → fullname should reflect change
    emp1.firstname = "Alicia"
    emp1.lastname = "Smyth"
    assert emp1.fullname() == "Alicia Smyth"


def test_email_reflects_current_names(module_banner, emp_pair):
    print("[test_email_reflects_current_names] running")
    _, emp2 = emp_pair

    # Initial email
    assert emp2.email() == "bob.brown@company.com"

    # Scenario: after marriage, last name changes
    emp2.lastname = "Williams"
    assert emp2.email() == "bob.williams@company.com"


def test_apply_raise_uses_class_attribute_and_is_overridable(emp_pair):
    """
    Similar scenario as unittest version:
    - Temporarily change Employee.salary_raise inside this test
    - Ensure it's restored afterwards
    """
    print("[test_apply_raise_uses_class_attribute_and_is_overridable] running")
    emp1, emp2 = emp_pair

    # Save original class attribute
    original_raise = Employee.salary_raise
    try:
        # Change class attribute only for this test
        Employee.salary_raise = 1.20  # 20% raise

        emp1.apply_raise()
        assert emp1.salary == 72000.0  # 60000 * 1.20

        emp2.apply_raise()
        assert emp2.salary == 54000.0  # 45000 * 1.20
    finally:
        # Restore original to avoid impacting other tests
        Employee.salary_raise = original_raise


# ==============================================================
# SECTION C: Demonstrating order & setup/teardown prints
# ==============================================================

@pytest.fixture(scope="module")
def order_module_banner():
    """
    Separate module-level banner for the 'order' section.
    Helps visually separate this group of tests in the output.
    """
    print("\n=== [order_module_banner] ORDER TESTS MODULE SETUP ===")
    yield
    print("=== [order_module_banner] ORDER TESTS MODULE TEARDOWN ===")


@pytest.fixture
def emp_for_order():
    """
    Per-test fixture (like setUp/tearDown) for order demonstration tests.
    """
    print("[emp_for_order] setUp-like for order test")
    emp = Employee("Test", "Order", 10000)
    yield emp
    print("[emp_for_order] tearDown-like for order test")
    del emp


def test_a_fullname(order_module_banner, emp_for_order):
    """
    Naming tests as test_a_*, test_b_* ensures the execution order
    (pytest runs tests in file order by default, but many devs also
     use alphabetical naming to make the order obvious in teaching demos).
    """
    print("[test_a_fullname] running")
    assert emp_for_order.fullname() == "Test Order"


def test_b_email(order_module_banner, emp_for_order):
    print("[test_b_email] running")
    assert emp_for_order.email() == "test.order@company.com"


def test_c_raise(order_module_banner, emp_for_order):
    print("[test_c_raise] running")

    original_raise = Employee.salary_raise
    try:
        Employee.salary_raise = 1.50
        emp_for_order.apply_raise()
        assert emp_for_order.salary == 15000.0
    finally:
        Employee.salary_raise = original_raise


"""
-------------------------------------------------------------
HOW TO RUN (PYTEST)
-------------------------------------------------------------

From the folder containing this file:

1) Run all tests:
    pytest
    pytest -v

2) Run only this file:
    pytest test_employee_pytest_functions.py
    pytest test_employee_pytest_functions.py -v

3) Run specific tests:
    pytest test_employee_pytest_functions.py::test_fullname_manual
    pytest test_employee_pytest_functions.py::test_a_fullname

WHAT TO OBSERVE IN OUTPUT:
- For fixture-based tests:
    - module_fixture setup prints once (like setUpClass)
    - per-test fixture setup prints before each test (like setUp)
    - test prints show which test is running
    - per-test fixture teardown prints after each test (like tearDown)
    - module_fixture teardown prints once at end (like tearDownClass)

SCENARIOS :
- Why fixtures are better than setUp/tearDown in many cases
    Because fixtures are reusable, modular, and explicit — they only run when a test asks for them, 
    unlike setUp/tearDown which run for every test whether needed or not.

- How scope="module" compares to setUpClass/tearDownClass
    A scope="module" fixture runs once per test file (module), while setUpClass/tearDownClass run once 
    per test class; module-scope covers more tests with fewer setups.
    
- How to safely modify class attributes inside tests
    Store the original value, modify it for the test, then restore it in a finally block or using pytest’s 
    addCleanup / fixture teardown so other tests remain unaffected.

- Why tests should remain independent and order-agnostic, even
  when we demonstrate order visually with names/prints.
    Because each test must work even if executed alone or in any order; dependent tests create hidden 
    coupling and break reliably when the environment or order changes.
  
  
  
  
  
  
  unittest                pytest
--------------------------------------------------------
setUp()             →   fixture (function scope)
tearDown()          →   fixture (after yield)
setUpClass()        →   fixture (class scope)
tearDownClass()     →   fixture (after yield, class scope)
No direct equivalent →  fixture(scope="module")
No direct equivalent →  fixture(scope="session")

-------------------------------------------------------------
"""
