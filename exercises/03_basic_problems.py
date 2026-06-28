"""
Exercise 3: Basic Problem Solving
Topics covered:
- Finding maximum value
- List operations
- Loops and iterations
- Mathematical calculations
"""


def find_largest(numbers):
    """
    Find the largest number from a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: The largest number
    """
    return max(numbers)


def sum_of_natural_numbers(n):
    """
    Calculate the sum of first n natural numbers using formula.
    
    Args:
        n (int): Number of natural numbers to sum
        
    Returns:
        int: Sum of first n natural numbers
        
    Formula: n * (n + 1) / 2
    """
    return (n * (n + 1)) // 2


def multiplication_table(n, limit=10):
    """
    Generate multiplication table for a number.
    
    Args:
        n (int): Number to multiply
        limit (int): How many multiples to generate (default: 10)
        
    Returns:
        list: List of results
    """
    return [n * i for i in range(1, limit + 1)]


def remove_item_from_list(items, item_to_remove):
    """
    Remove an item from a list.
    
    Args:
        items (list): Original list
        item_to_remove: Item to be removed
        
    Returns:
        list: Modified list without the item
    """
    if item_to_remove in items:
        items.remove(item_to_remove)
    return items


def print_numbers_in_line(numbers):
    """
    Print numbers in a single line separated by spaces.
    
    Args:
        numbers (list): List of numbers to print
    """
    for num in numbers:
        print(num, end=" ")
    print()  # New line at the end


def run_basic_problem_exercises():
    """Run all basic problem-solving exercises."""
    print("=" * 50)
    print("BASIC PROBLEM SOLVING EXERCISES")
    print("=" * 50)
    
    # Exercise 1: Find Largest Number
    print("\n1. Find Largest Number")
    print("-" * 30)
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    largest = find_largest([num1, num2, num3])
    print(f"The largest number is: {largest}")
    
    # Exercise 2: Sum of Natural Numbers
    print("\n2. Sum of First N Natural Numbers")
    print("-" * 30)
    n = int(input("Enter a number: "))
    if n > 0:
        total = sum_of_natural_numbers(n)
        print(f"The sum of the first {n} natural numbers is: {total}")
    else:
        print("Please enter a positive number.")
    
    # Exercise 3: Multiplication Table
    print("\n3. Multiplication Table")
    print("-" * 30)
    num = int(input("Enter a number to multiply: "))
    table = multiplication_table(num)
    print(f"Multiplication table of {num}:")
    for i, result in enumerate(table, 1):
        print(f"{num} x {i} = {result}")
    
    # Exercise 4: Print Numbers in Line
    print("\n4. Print Numbers in a Line")
    print("-" * 30)
    numbers = [10, 20, 30, 40]
    print_numbers_in_line(numbers)
    
    # Exercise 5: Remove Item from List
    print("\n5. Remove Item from List")
    print("-" * 30)
    fruits = ["apple", "banana", "cherry"]
    print(f"Original list: {fruits}")
    item = input("Enter an item to remove: ")
    updated_list = remove_item_from_list(fruits.copy(), item)
    print(f"Updated list: {updated_list}")


if __name__ == "__main__":
    run_basic_problem_exercises()
