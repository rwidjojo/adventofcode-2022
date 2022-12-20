from typing import List, Set

with open("data/day3.txt", "r") as file:
    data = file.read().split("\n")


def letter_to_number(char: str):
    if char.isupper():
        return ord(char) - 64 + 26

    return ord(char) - 96


def get_intersecting_letter(word: List[Set[str]]):
    intersection = set.intersection(*word)

    return list(intersection)[0]


totals_one = 0
totals_two = 0

for line in data:
    word_length = len(line)
    intersecting_letter = get_intersecting_letter([set(line[: word_length // 2]), set(line[word_length // 2 :])])
    totals_one += letter_to_number(intersecting_letter)

while len(data) > 0:
    first = set(data.pop())
    second = set(data.pop())
    third = set(data.pop())
    intersecting_letter = get_intersecting_letter([first, second, third])
    totals_two += letter_to_number(intersecting_letter)

print(f"Solution 1: {totals_one}")
print(f"Solution 2: {totals_two}")
