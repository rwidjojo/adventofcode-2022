with open("data/day2.txt", "r") as file:
    data = file.read().split("\n")

FIRST_SCORE_MAP = {
    "A X": 1 + 3,  # rock rock
    "A Y": 2 + 6,  # rock paper
    "A Z": 3 + 0,  # rock scissors
    "B X": 1 + 0,  # paper rock
    "B Y": 2 + 3,  # paper paper
    "B Z": 3 + 6,  # paper scissors
    "C X": 1 + 6,  # scissors rock
    "C Y": 2 + 0,  # scissors paper
    "C Z": 3 + 3,  # scissors scissors
}

SECOND_SCORE_MAP = {
    "A X": 0 + 3,  # lose to rock -> scissors
    "A Y": 3 + 1,  # draw to rock -> rock
    "A Z": 6 + 2,  # win to rock -> paper
    "B X": 0 + 1,  # lose to paper -> rock
    "B Y": 3 + 2,  # draw to paper -> paper
    "B Z": 6 + 3,  # win to paper -> scissors
    "C X": 0 + 2,  # lose to scissors -> paper
    "C Y": 3 + 3,  # draw to scissors -> scissors
    "C Z": 6 + 1,  # win to scissors -> rock
}

totals_one = sum(FIRST_SCORE_MAP[item] for item in data)
totals_two = sum(SECOND_SCORE_MAP[item] for item in data)

print(f"Solution 1: {totals_one}")
print(f"Solution 2: {totals_two}")
