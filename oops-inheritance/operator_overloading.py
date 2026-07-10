# operator_overloading.py
# Demonstrates operator overloading in Python using __add__

class Number:
    def __init__(self, n):
        self.n = n

    # Overloading the '+' operator
    def __add__(self, other):
        return self.n + other.n

    # String representation for easy printing
    def __str__(self):
        return str(self.n)


# Object creation
n = Number(5)
m = Number(10)

# Using overloaded '+' operator
print(n + m)   # Output: 15

# Printing objects directly
print("n =", n)  # Output: n = 5
print("m =", m)  # Output: m = 10
