# Question 8: Compare two files for identical content

# Read first file
with open("hi-score.txt", "r") as f:
    content = f.read()

# Read second file
with open("high_score.txt", "r") as f:
    data = f.read()

# Compare content
if content == data:
    print("Files are identical")
else:
    print("Files are not identical")
