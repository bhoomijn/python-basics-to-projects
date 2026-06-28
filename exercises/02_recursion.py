"""
Exercise 2: Recursion
Topics covered:
- Recursive function definition
- Base case and recursive case
- Factorial calculation
- Pattern generation using recursion
"""


def factorial(n):
    """
    Calculate factorial of n using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Examples:
        factorial(5) = 120
        factorial(0) = 1
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def print_star_pattern(n):
    """
    Print a decreasing star pattern using recursion.
    
    Args:
        n (int): Number of stars in the first line
        
    Examples:
        print_star_pattern(3) prints:
        ***
        **
        *
    """
    if n == 0:
        return
    print("*" * n)
    print_star_pattern(n - 1)


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Examples:
        fibonacci(5) = 5
        fibonacci(6) = 8
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base, exponent):
    """
    Calculate base raised to the power of exponent using recursion.
    
    Args:
        base (float): Base number
        exponent (int): Exponent (non-negative)
        
    Returns:
        float: Result of base^exponent
        
    Examples:
        power(2, 5) = 32
        power(3, 3) = 27
    """
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def run_recursion_exercises():
    """Run all recursion exercises."""
    print("=" * 50)
    print("RECURSION EXERCISES")
    print("=" * 50)
    
    # Exercise 1: Factorial
    print("\n1. Factorial Calculation")
    print("-" * 30)
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
    
    # Exercise 2: Star Pattern
    print("\n2. Star Pattern Generation")
    print("-" * 30)
    num = int(input("Enter number of stars: "))
    if num > 0:
        print_star_pattern(num)
    else:
        print("Please enter a positive number.")
    
    # Exercise 3: Fibonacci
    print("\n3. Fibonacci Sequence")
    print("-" * 30)
    num = int(input("Enter position in Fibonacci sequence: "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        result = fibonacci(num)
        print(f"Fibonacci number at position {num} is: {result}")
    
    # Exercise 4: Power
    print("\n4. Power Calculation")
    print("-" * 30)
    base = float(input("Enter base number: "))
    exponent = int(input("Enter exponent: "))
    if exponent < 0:
        print("Please enter a non-negative exponent.")
    else:
        result = power(base, exponent)
        print(f"{base}^{exponent} = {result}")


if __name__ == "__main__":
    run_recursion_exercises()
