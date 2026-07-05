# instance_vs_classattribute.py
class employe:
    language = "Python"   # class attribute
    salary = 10000        # class attribute

harry = employe()         # instance of class employe
harry.salary = 12000      # instance attribute
print(harry.salary, harry.language)  # Output: 12000 Python
