# Python Practice 🐍

Daily Python practice codes and mini projects — documenting my learning journey before starting M.Tech AIML at VIT Bhopal.

## 📁 Project Structure

```
python-practice/
├── exercises/              # Package containing all exercise modules
│   ├── __init__.py
│   ├── 01_functions.py     # Function definition and parameters
│   ├── 02_recursion.py     # Recursive functions and patterns
│   └── 03_basic_problems.py # Basic problem-solving exercises
├── main.py                 # Main entry point with interactive menu
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

## 📚 Topics Covered

### 1. Functions (`exercises/01_functions.py`)
- Function definition and calling
- Function parameters and return values
- Default parameters
- Practical exercises:
  - Average calculator
  - Temperature conversion (Celsius → Fahrenheit)
  - Unit conversion (Inches → Centimeters)
  - Greeting function with customizable messages

### 2. Recursion (`exercises/02_recursion.py`)
- Recursive function definition
- Base case and recursive case concept
- Practical exercises:
  - Factorial calculation
  - Star pattern generation
  - Fibonacci sequence
  - Power calculation using recursion

### 3. Basic Problem Solving (`exercises/03_basic_problems.py`)
- Finding maximum values
- List operations
- Loops and iterations
- Mathematical calculations
- Practical exercises:
  - Finding the largest number
  - Sum of natural numbers
  - Multiplication table generation
  - List manipulation

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the Program

**Option 1: Interactive Menu (Recommended)**
```bash
python main.py
```
This will open an interactive menu where you can:
- Run individual exercise categories
- Run all exercises in sequence
- Exit the program

**Option 2: Run Individual Exercise Files**
```bash
# Run only functions exercises
python exercises/01_functions.py

# Run only recursion exercises
python exercises/02_recursion.py

# Run only basic problem solving exercises
python exercises/03_basic_problems.py
```

## 📝 Example Usage

```python
from exercises.functions import calculate_average, celsius_to_fahrenheit

# Use functions directly in your code
avg = calculate_average(10, 20)  # Returns 15.0
temp_f = celsius_to_fahrenheit(25)  # Returns 77.0
```

## 🎯 Key Features

✅ **Well-Organized Code** - Separated by topics in different modules  
✅ **Proper Documentation** - Docstrings for all functions  
✅ **Error Handling** - Input validation for all exercises  
✅ **Interactive Menu** - User-friendly way to run exercises  
✅ **Reusable Functions** - All functions return values, not just print  
✅ **Comments** - Clear explanations throughout the code  

## 📖 Code Improvements Made

This refactored version includes:

1. **Removed Duplicates** - Eliminated repeated code
2. **Better Naming** - Clear, descriptive variable and function names
3. **Return Values** - Functions return results instead of just printing
4. **Docstrings** - Professional documentation for all functions
5. **Type Hints Ready** - Structure supports easy addition of type hints
6. **Error Handling** - Input validation to prevent crashes
7. **Modular Design** - Each topic in a separate, manageable file
8. **Bug Fixes** - Fixed string comparison issues in original code

## 🔄 Future Enhancements

- [ ] Add type hints to all functions
- [ ] Add unit tests using pytest
- [ ] Create advanced exercises (OOP, file handling, data structures)
- [ ] Add example outputs in documentation
- [ ] Create a comprehensive test suite

## 📚 Learning Goals

- Master Python fundamentals
- Understand function design principles
- Learn recursion and when to use it
- Develop problem-solving skills
- Write clean, maintainable code

## 👤 Author

**bhoomijn**  
Preparing for M.Tech AIML at VIT Bhopal

## 📄 License

This project is open source and available under the MIT License.

---

**Last Updated:** June 28, 2026  
**Status:** Active Learning 🎓
