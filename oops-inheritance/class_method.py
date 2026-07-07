# class_method.py
# Example of class method vs instance method in Python OOP

class Employee:
    a = 1

    @classmethod
    def show_class(cls):
        """Class method: always uses class attribute"""
        print(f"This is Employee class {cls.a}")

    def show_instance(self):
        """Instance method: can use instance attribute"""
        print(f"This is Employee instance {self.a}")


if __name__ == "__main__":
    e = Employee()
    e.a = 45

    # Class method → still prints class attribute (1)
    e.show_class()

    # Instance method → prints instance attribute (45)
    e.show_instance()
