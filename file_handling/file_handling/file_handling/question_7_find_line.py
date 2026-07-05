# Question 7: Find line number of '44'

i = 1
found = False

with open("hi-score.txt", "r") as f:
    for line in f:
        if "44" in line:
            print(f"44 found in line {i}")
            found = True
        i += 1

if not found:
    print("44 not found in any line")
