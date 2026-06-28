"""
Python Practice - Main Entry Point
A comprehensive collection of Python practice exercises for learning.

Author: bhoomijn
Purpose: Documentation of learning journey before M.Tech AIML at VIT Bhopal
"""

from exercises.01_functions import run_function_exercises
from exercises.02_recursion import run_recursion_exercises
from exercises.03_basic_problems import run_basic_problem_exercises


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("PYTHON PRACTICE - MAIN MENU")
    print("=" * 50)
    print("1. Function Exercises")
    print("2. Recursion Exercises")
    print("3. Basic Problem Solving")
    print("4. Run All Exercises")
    print("0. Exit")
    print("=" * 50)


def main():
    """Main function to run the program."""
    print("\n" + "🐍 " * 15)
    print("Welcome to Python Practice!")
    print("Learning journey before M.Tech AIML at VIT Bhopal")
    print("🐍 " * 15)
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == "1":
            run_function_exercises()
        elif choice == "2":
            run_recursion_exercises()
        elif choice == "3":
            run_basic_problem_exercises()
        elif choice == "4":
            run_function_exercises()
            input("\n\nPress Enter to continue to next exercise...")
            run_recursion_exercises()
            input("\n\nPress Enter to continue to next exercise...")
            run_basic_problem_exercises()
        elif choice == "0":
            print("\n" + "=" * 50)
            print("Thank you for practicing Python!")
            print("Keep learning and coding! 🚀")
            print("=" * 50 + "\n")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 0 and 4.")
        
        if choice in ["1", "2", "3"]:
            continue_choice = input("\n\nDo you want to continue? (yes/no): ").strip().lower()
            if continue_choice not in ["yes", "y"]:
                print("\nThank you for practicing! See you next time! 👋\n")
                break


if __name__ == "__main__":
    main()
