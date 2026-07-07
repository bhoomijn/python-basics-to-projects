# super_constructor.py
# Example of using super() in inheritance chain

class Employee:
    def __init__(self):
        print("This is Employee class")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()   # calls Employee constructor
        print("This is Programmer class")
    b = 2

class Coder(Programmer):
    def __init__(self):
        super().__init__()   # calls Programmer (and indirectly Employee)
        print("This is Coder class")
    c = 3

if __name__ == "__main__":
    o = Coder()
    print("Coder attribute c:", o.c)
