import re
from typing import List

with open("../data/day5.txt", "r") as file:
    puzzle, moves = file.read().split("\n\n")


def load_stack(puzzle_input: str):
    lines = puzzle_input.split("\n")
    max_length = max(map(lambda x: len(x), lines))
    # prepare vertical stack to store the inputs
    # assume that the format is [X] [Y] [Z] ...
    # the number of stack = max_length // 4 + 1
    vertical_stacks = [[] for _ in range(max_length // 4 + 1)]

    for line in lines[:-1]:
        for i in range(max_length // 4 + 1):
            if line[4 * i + 1] == " ":
                continue

            vertical_stacks[i].append(line[4 * i + 1])

    return vertical_stacks


def process_move_9000(input_stack: List[List[str]], move: str, multiple_flag: bool = False):
    count, stack_from, stack_to = re.search(r"move (\d+) from (\d+) to (\d+)", move).groups()
    temp_stack = []
    for _ in range(int(count)):
        # get top most element from source stack and append to a temporary stack
        popped = input_stack[int(stack_from) - 1].pop(0)
        temp_stack.append(popped)

    if not multiple_flag:
        temp_stack.reverse()

    input_stack[int(stack_to) - 1] = temp_stack + input_stack[int(stack_to) - 1]
    return input_stack


stack_one = load_stack(puzzle)
stack_two = load_stack(puzzle)

for move in moves.split("\n"):
    stack_one = process_move_9000(stack_one, move, multiple_flag=False)
    stack_two = process_move_9000(stack_two, move, multiple_flag=True)

first_top_elements = "".join(map(lambda x: x[0], stack_one))
second_top_elements = "".join(map(lambda x: x[0], stack_two))

print(f"Solution 1: {first_top_elements}")
print(f"Solution 2: {second_top_elements}")
