# Question 4: Replace word in file

word = "100"

# Read the file
with open("high_score.txt", "r") as f:
    content = f.readlines()

# Replace occurrences of 'word' with '10'
content_new = []
for line in content:
    content_new.append(line.replace(word, "10"))

# Write updated content back to file
with open("high_score.txt", "w") as f:
    f.writelines(content_new)
