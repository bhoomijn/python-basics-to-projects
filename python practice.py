# function and recursions

print("Hello, World!")
# function definition
def avg():
    a=int(input("Enter the first number: "))
    b=int(input("Enter a number: "))
    avg=(a+b)/2
    print(avg)
avg()

print("Hello, World!")
# function definition
def avg():
    a=int(input("Enter the first number: "))
    b=int(input("Enter a number: "))
    avg=(a+b)/2
    print(avg)
# function call
avg()
print("This is a simple program to calculate the average of two numbers.")
print("Thank you for using this program!")
avg()

# quick quiz

name=input("Enter your name: ")
print("Hello, " + name + "! Welcome to the quiz.")

# quick quiz

def GoodDay():
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to the quick quiz.")

GoodDay()

# functions with arguments

def GoodDay(name, ending = "thank you"):
    print(f"Hello, {name}{ending} Welcome to the quick quiz.")

GoodDay(" Alice")

def GoodDay(name, ending = "thank you"):
    print(f"Hello,{name}!")
    print(ending)
GoodDay(" Alice")

# Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter a number to calculate its factorial: "))
print(factorial(n))



