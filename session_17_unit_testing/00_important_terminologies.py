"""
------------------------------------------------------------
TESTING — FOUNDATIONAL NOTES
------------------------------------------------------------

1) WHY WE NEED TESTING (Scenarios)
----------------------------------
- To ensure our code works as intended after every change.
- To detect bugs early before deployment (cheaper to fix).
- To verify that new features don't break existing functionality (regression).
- To validate business logic across multiple input scenarios.
- To provide confidence during refactoring or optimization.
- To support CI/CD pipelines where automated tests run before merging code.
- To make collaborative projects reliable and maintainable.

EXAMPLES / SCENARIOS:
- A function that calculates discounts → ensure correct output for all price ranges.
- A database connection handler → ensure retry logic works on failure.
- A data pipeline → ensure schema validation and record counts remain correct after code changes.

------------------------------------------------------------

2) WHAT IS UNIT TESTING
-----------------------
- Unit testing is the process of testing **individual pieces (units)** of code in isolation.
- Each test checks a single behavior or functionality.
- Goal: confirm that each function/class works correctly and independently.
- Typically automated using frameworks like `unittest`, `pytest`, or `nose2`.
- Helps identify which exact part of the code fails when something breaks.

EXAMPLE:
    def add(a, b):
        return a + b

    # Unit Test
    def test_add():
        assert add(2, 3) == 5

------------------------------------------------------------

3) WHAT ARE UNITS
-----------------
- A **unit** is the smallest testable part of a program.
- Usually a single function, method, or class.
- Each unit should perform one logical task and can be tested independently.
- In large projects, units combine to form modules, and modules combine to form systems.

EXAMPLES:
- A function: `calculate_tax()`
- A method inside a class: `Customer.get_full_name()`
- A small reusable component: `DatabaseConnector.connect()`

------------------------------------------------------------
"""
