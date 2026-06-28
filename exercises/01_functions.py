"""
Exercise 1: Functions
Topics covered:
- Function definition and calling
- Function parameters
- Return values
- Default parameters
"""


def calculate_average(num1, num2):
    """
    Calculate the average of two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: Average of the two numbers
    """
    return (num1 + num2) / 2


def greet_user(name, greeting="Hello"):
    """
    Greet a user with a personalized message.
    
    Args:
        name (str): Name of the user
        greeting (str): Custom greeting message (default: "Hello")
        
    Returns:
        str: Formatted greeting message
    """
    return f"{greeting}, {name}! Welcome to the quick quiz."


def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def inches_to_centimeters(inches):
    """
    Convert length from inches to centimeters.
    
    Args:
        inches (float): Length in inches
        
    Returns:
        float: Length in centimeters
    """
    return inches * 2.54


def run_function_exercises():
    """Run all function exercises."""
    print("=" * 50)
    print("FUNCTION EXERCISES")
    print("=" * 50)
    
    # Exercise 1: Average Calculator
    print("\n1. Average Calculator")
    print("-" * 30)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    avg = calculate_average(num1, num2)
    print(f"Average: {avg}")
    
    # Exercise 2: Greeting with default parameter
    print("\n2. Greeting Function")
    print("-" * 30)
    name = input("What is your name? ")
    print(greet_user(name))
    print(greet_user(name, "Hi"))
    
    # Exercise 3: Temperature Conversion
    print("\n3. Celsius to Fahrenheit")
    print("-" * 30)
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    
    # Exercise 4: Unit Conversion
    print("\n4. Inches to Centimeters")
    print("-" * 30)
    inches = float(input("Enter length in inches: "))
    centimeters = inches_to_centimeters(inches)
    print(f"{inches} inches = {centimeters} cm")


if __name__ == "__main__":
    run_function_exercises()
