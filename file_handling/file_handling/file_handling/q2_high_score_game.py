import random

def game():
    score = random.randint(1, 60)
    print("You are playing a game")
    print(f"Your score is {score}")

    # File open in read mode
    try:
        with open("high_score.txt", "r") as f:
            high_score = f.read()
        if high_score == "":
            high_score = 0
        else:
            high_score = int(high_score)
    except FileNotFoundError:
        high_score = 0

    # Compare score
    if score > high_score:
        print("🎉 New High Score!")
        with open("high_score.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"High score remains {high_score}")

    return score

# Run the game
if __name__ == "__main__":
    game()
