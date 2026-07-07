# single_inheritance.py
# Example of single and multilevel inheritance in Python OOP

class Employee:
    a = 1

class Programmer(Employee):   # inherits Employee
    b = 2

class Coder(Programmer):      # inherits Programmer (and indirectly Employee)
    c = 3

if __name__ == "__main__":
    o = Programmer()
    print("Employee attribute a:", o.a)   # 1
    print("Programmer attribute b:", o.b) # 2

    c = Coder()
    print("Coder attribute c:", c.c)      # 3
    print("Coder inherited a:", c.a)      # 1
    print("Coder inherited b:", c.b)      # 2
