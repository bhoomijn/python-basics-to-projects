# instance_vs_classattribute.py
class employe:
    language = "Python"  # class attribute
    salary = 10000       # class attribute

    def getInfo(self):
        print(f"Salary: {self.salary}, Language: {self.language}")

    def greet(self):
        print("Hello, welcome to the company!")

harry = employe()        # instance of class employe
harry.salary = 12000     # instance attribute
harry.getInfo()          # Output: Salary: 12000, Language: Python
harry.greet()            # Output: Hello, welcome to the company!
