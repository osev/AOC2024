from collections import Counter, defaultdict
from itertools import permutations

test_input = "125 17"
problem_input = "4022724 951333 0 21633 5857 97 702 6"


def parse_input(current_input):
    current_input = current_input.split(" ")
    return current_input


stones = parse_input(problem_input)


def process_blink(val):
    if stone == "0":
        return ["1"]

    if len(stone) % 2 == 0:
        middle = len(stone) // 2
        return [str(int(stone[:middle])), str(int(stone[middle:]))]

    return [str(int(stone) * 2024)]


stones = Counter(stones)
for blink in range(75):
    next_round = defaultdict(int)

    for stone, count in stones.items():
        for blink_stone in process_blink(stone):
            next_round[blink_stone] += count

    stones = next_round

print(sum(stones.values()))
