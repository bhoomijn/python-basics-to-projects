# property_decorator_example.py
# Demonstrates use of @property and @classmethod in Python

class Employee:
    a = 1  # class attribute

    @classmethod
    def show(cls):
        print(f"This is show method {cls.a}")

    def __init__(self):
        self._name = "Harry"

    # Getter method using @property
    @property
    def name(self):
        return self._name

    # Setter method using @name.setter
    @name.setter
    def name(self, value):
        self.fname = value.split()[0]
        self.lname = value.split()[1]
        self._name = value


# Object creation
e = Employee()

# Changing instance attribute
e.a = 45

# Using property setter
e.name = "John Doe"

# Printing property value
print(e.name)  # Output: John Doe

# Calling class method
e.show()       # Output: This is show method 1
