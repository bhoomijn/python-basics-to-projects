# Question 6: Search for a word in file

# Open the file and read content
with open("high_score.txt", "r") as f:
    high_scores = f.read()

# Check if 'python' exists (case-insensitive)
if "python" in high_scores.lower():
    print("Python is in the high scores.")
else:
    print("Python is not in the high scores.")
