from collections import defaultdict
from itertools import permutations

test_input = "125 17"
problem_input = "4022724 951333 0 21633 5857 97 702 6"


def parse_input(current_input):
    current_input = current_input.split(" ")
    return current_input


stones = parse_input(problem_input)

for blink in range(25):
    next_round = []
    for i, stone in enumerate(stones):
        if stone == "0":
            next_round.append("1")
            continue

        if len(stone) % 2 == 0:
            middle = len(stone) // 2
            next_round.append(str(int(stone[:middle])))
            next_round.append(str(int(stone[middle:])))
            continue

        next_round.append(str(int(stone) * 2024))
    stones = next_round

print(len(stones))
