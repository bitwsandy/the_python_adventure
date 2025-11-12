# employee.py
# --------------------------------------------------------------
# EMPLOYEE CLASS (Code Under Test)
# --------------------------------------------------------------
# Notes:
# - Instance attributes: firstname, lastname, salary
# - Class attribute: salary_raise (a multiplier applied by apply_raise)
# - Instance methods:
#     fullname() -> "<firstname> <lastname>"
#     email()    -> "<firstname>.<lastname>@company.com" (lowercased)
#     apply_raise() -> updates salary in-place using class attr
#
# Design choices:
# - Keep logic intentionally simple for unit testing demonstration.
# - email() uses the current names (so if names change, email() output changes).
# --------------------------------------------------------------

class Employee:
    # Class attribute used by apply_raise
    salary_raise = 1.10  # 10% default raise

    def __init__(self, firstname: str, lastname: str, salary: float):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = float(salary)

    def fullname(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def email(self) -> str:
        # Lowercase, simple domain for demo
        return f"{self.firstname}.{self.lastname}@company.com".lower()

    def apply_raise(self) -> None:
        # Uses the CLASS attribute (Employee.salary_raise)
        # Not an instance attribute, so tests can override it temporarily
        self.salary *= self.salary_raise
