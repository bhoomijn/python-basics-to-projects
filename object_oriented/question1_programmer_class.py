# question1_programmer_class.py
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project

# First object
p = Programmer("Harry", "50000", "project1")
print(p.name, p.salary, p.project)

# Second object
r = Programmer("Rohan", "60000", "project2")
print(r.name, r.salary, r.project)
