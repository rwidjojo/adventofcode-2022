from typing import Optional

with open("../data/day6.txt", "r") as file:
    packet = list(file.read())


def get_marker(string_packet: str, distinct_char_count: int) -> Optional[int]:
    temp_list = [None for _ in range(distinct_char_count)]
    counter = 0

    while True:
        if len(string_packet) == 0:
            return None

        entry = string_packet.pop(0)
        counter += 1
        temp_list.append(entry)
        temp_list.pop(0)

        if len(set(temp_list)) == distinct_char_count:
            return counter


print(f"Solution 1: {get_marker(packet.copy(), 4)}")
print(f"Solution 2: {get_marker(packet.copy(), 14)}")
