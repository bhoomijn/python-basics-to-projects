# Question 8: Copy content from one file to another

# Read from source file
with open("hi-score.txt", "r") as f:
    content = f.readlines()

# Write into destination file
with open("high_score.txt", "w") as f:
    f.writelines(content)
