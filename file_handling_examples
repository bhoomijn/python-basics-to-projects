# file_handling_examples.py
# Collection of different file handling methods in Python
# You can keep adding more examples in this file

# -------------------------------
# Example 1: Using readlines()
# -------------------------------
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Using readlines():")
    print(lines, type(lines))
    print()

# -------------------------------
# Example 2: Using read()
# -------------------------------
with open("file.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print("Using read():")
    print(data)
    print(type(data))
    print()

# -------------------------------
# Example 3: Using readline()
# -------------------------------
with open("file.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    print("Using readline() - line1:")
    print(line1, type(line1))

    line2 = f.readline()
    print("Using readline() - line2:")
    print(line2, type(line2))


# file_handling_examples.py
# Collection of different file handling methods in Python

# -------------------------------
# Example 4: Reading file line by line using while loop
# -------------------------------
f = open("file.txt", "r", encoding="utf-8")
line = f.readline()
while line != "":
    print(line.strip())   # strip() removes extra newline
    line = f.readline()
f.close()

print()  # blank line for clarity

# -------------------------------
# Example 5: Reading entire file using with block
# -------------------------------
with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())

