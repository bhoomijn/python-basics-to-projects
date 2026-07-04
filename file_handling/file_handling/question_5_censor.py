# Question 5: Replace specific words with #

words = ("10", "donkey", "vim", "sabun")

# Read the file as a single string
with open("high_score.txt", "r") as f:
    content = f.read()

# Replace each word with '#' characters of same length
for word in words:
    content = content.replace(word, "#" * len(word))

# Write updated content back to file
with open("high_score.txt", "w") as f:
    f.write(content)
