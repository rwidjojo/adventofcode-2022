with open("../data/day1.txt", "r") as file:
    data = file.read().split("\n\n")

totals = []

for elf in data:
    totals.append(sum(map(lambda x: int(x), elf.split("\n"))))

totals_sorted = sorted(totals, reverse=True)

print(f"Solution 1: {max(totals_sorted)}")
print(f"Solution 2: {sum(totals_sorted[:3])}")
