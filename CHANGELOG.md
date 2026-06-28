## Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### [1.0.0] - 2026-06-28

#### Added
- Initial project structure with organized exercise modules
- Three main exercise categories:
  - Functions (01_functions.py) - Function definition, parameters, return values
  - Recursion (02_recursion.py) - Recursive functions, patterns, Fibonacci
  - Basic Problem Solving (03_basic_problems.py) - List ops, loops, calculations
- Interactive menu system in main.py
- Professional documentation and docstrings for all functions
- Comprehensive README.md with setup and usage instructions
- .gitignore for Python projects
- Unit tests for all modules using pytest
- GitHub Actions CI/CD pipeline for automated testing
- Issue templates (bug reports, feature requests)
- Pull request template with contribution checklist
- CONTRIBUTING.md with contribution guidelines

#### Improved
- Code organization: Separated monolithic file into focused modules
- Function design: All functions now return values for reusability
- Documentation: Added detailed docstrings with examples
- User experience: Interactive menu system for better navigation

#### Fixed
- String comparison bug in largest number finder
- Removed duplicate function definitions
- Fixed variable shadowing issues

#### Removed
- Redundant code from original python practice.py
- Unnecessary print statements