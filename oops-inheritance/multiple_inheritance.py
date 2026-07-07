# multiple_inheritance.py
# Example of Multiple Inheritance in Python OOP

class Employee:
    company = "Google"
    def showDetails(self):
        print(f"The name of the company is {self.company}")

class Programmer:
    company = "Microsoft"
    language = "Python"
    def getLanguage(self):
        print(f"The language is {self.language}")

class Coding(Programmer, Employee):   # multiple inheritance
    name = "Rohit"
    def showDetails(self):
        print(f"The name of the company is {self.company}")
        print(f"The name of the employee is {self.name}")

if __name__ == "__main__":
    a = Employee()
    b = Programmer()
    c = Coding()
    print(a.company, b.company, c.name)   # Google Microsoft Rohit
    c.showDetails()
