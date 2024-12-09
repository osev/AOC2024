from collections import defaultdict
from itertools import permutations

test_input = "2333133121414131402"


def parse_input(current_input):
    current_input = list(current_input)
    return [int(val) for val in current_input]


def get_blocks(dense):
    blocks = []
    file_id = 0

    for i, space in enumerate(dense):
        if i % 2 != 0:
            blocks += ["."] * space
            continue

        blocks += [file_id] * space
        file_id += 1

    return blocks


def sort_blocks(blocks):
    left, right = 0, len(blocks) - 1

    while left < right:
        if blocks[left] != ".":
            left += 1
            continue
        if blocks[right] == ".":
            right -= 1
            continue

        current_left = left

        blocks[left], blocks[right] = blocks[right], blocks[left]
        left += 1
        right -= 1

    return blocks


def calculate_checksum(blocks):
    sum = 0

    for idx, file_id in enumerate(blocks):
        if file_id == ".":
            continue

        sum += idx * file_id

    return sum


text_file = open("src/day-9/input.txt", "r")
problem_input = text_file.read()

memory_input = parse_input(problem_input)
blocks = get_blocks(memory_input)
sorted_blocks = sort_blocks(blocks)
checksum = calculate_checksum(sorted_blocks)

print(checksum)
