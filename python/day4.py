from typing import List


def check_containment(list_one: List, list_two: List):
    one, two = list_one
    first, second = list_two

    if int(one) <= int(first) and int(two) >= int(second):
        return True

    if int(first) <= int(one) and int(second) >= int(two):
        return True

    return False


def check_overlap(list_one: List, list_two: List):
    one, two = list_one
    first, second = list_two

    if int(one) <= int(first) and int(first) <= int(two):
        return True

    if int(first) <= int(one) and int(one) <= int(second):
        return True

    return False


totals_one = 0
totals_two = 0

with open("data/day4.txt", "r") as file:
    for line in file:
        x, y = line.split(",")

        totals_one += check_containment(x.split("-"), y.split("-"))
        totals_two += check_overlap(x.split("-"), y.split("-"))

print(f"Solution 1: {totals_one}")
print(f"Solution 2: {totals_two}")
