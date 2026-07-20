
# employee_salary_increment.py
# Demonstrates use of @property decorator in Python

class Employee:
    salary = 2000
    increment = 500

    @property
    def salary_after_increment(self):
        return self.salary + self.salary * (self.increment) / 100


# Object creation
e = Employee()

# Accessing property like an attribute
print("Salary after increment:", e.salary_after_increment)
# Output: Salary after increment: 12000
