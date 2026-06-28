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

# Practice test

#question 1:

a=input("Enter a number: ")
b=input("Enter another number: ")
c=input("Enter a third number: ")

largest = max(a, b, c)
print("The largest number is:", largest)

# question 2:

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# question 2 in another way:

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")
print(f"{celsius}°C is equal to {fahrenheit}°F")

# This is a practice test for Python programming. The following code snippets will help you understand basic concepts and syntax in Python.

# question 3:

a = 10
b = 20
c = 30
d = 40

print(a , end = " ")
print(b , end = " ")
print(c , end = " ")
print(d)

# question 4

n = int(input("Enter a number: "))
sum = ( n * (n + 1)) // 2
print("The sum of the first", n, "natural numbers is:", sum)

# question 4 in another way :

def calculate_sum():
    n = int(input("Enter a number: "))
    sum = (n * (n + 1)) // 2
    print("The sum of the first", n, "natural numbers is:", sum)

calculate_sum()
calculate_sum()

# question 5

def pattern(n):
    if(n==0):
       return
    print("*" *n)
    pattern(n-1)

pattern(9)
pattern(100)

# question 6:

def inches_to_centimeters(inches):

    """
    Convert inches to centimeters.
    
    Parameters:
    inches (float): The length in inches to be converted.
    
    Returns:
    float: The length in centimeters.
    """
    centimeters = inches * 2.54
    return centimeters
print(inches_to_centimeters(7))  # This will print the result of converting 7 inches to centimeters 
print(inches_to_centimeters(5))  # This will print the result of converting 5 inches to centimeters

# question 7:

L = [1, 2, 3, 4, 5]

L.remove(3)
print(L)  # Output: [1, 2, 4, 5]

# question 7 in another way

l = ["apple", "banana", "cherry"]

def remove_item(item):
    l.remove(item)
    return l
item = input("Enter an item to remove from the list: ")
print(remove_item(item))  
