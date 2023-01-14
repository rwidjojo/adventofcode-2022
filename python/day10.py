from typing import List


def load_instruction() -> List[str]:
    with open("data/day10.txt", "r") as file:
        instructions = file.read()

    return instructions.split("\n")


def add_total(step, strength):
    if step % 40 == 20:
        return step * strength

    return 0


def get_signal_strength(signal_instructions: List[str], start_value: int = 1) -> int:
    step = 0
    strength = start_value
    total = 0

    for signal in signal_instructions:
        inst, *vals = signal.split(" ")

        if inst == "noop":
            step += 1
            total += add_total(step, strength)

        if inst == "addx":
            step += 1
            total += add_total(step, strength)

            step += 1
            total += add_total(step, strength)
            strength += int(vals[0])

    return total


ans_1 = get_signal_strength(load_instruction())
print(f"Solution 1: {ans_1}")
