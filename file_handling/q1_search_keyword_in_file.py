"""
Question 1: Search Keyword in File
-----------------------------------
Write a Python program that:
- Opens a file named 'file.txt'
- Searches for a specific keyword (e.g., "TWINKLE")
- Prints whether the keyword is found or not
- Properly handles file closing

Learning Objectives:
- File reading operations
- String search operations
- Conditional statements
- Resource management (with statement)
- Error handling
"""

def search_keyword_in_file(filename, keyword):
    """
    Search for a keyword in a file and display the result.
    
    Args:
        filename (str): Path to the file to search
        keyword (str): The keyword to search for
        
    Returns:
        bool: True if keyword is found, False otherwise
    """
    try:
        # Open and read file using 'with' statement (auto-closes)
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Check if keyword exists in file content
        if keyword in content:
            print(f"✓ '{keyword}' found in the file.")
            return True
        else:
            print(f"✗ '{keyword}' not found in the file.")
            return False
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


# Main Execution
if __name__ == "__main__":
    filename = "file.txt"
    keyword = "TWINKLE"
    
    search_keyword_in_file(filename, keyword)
