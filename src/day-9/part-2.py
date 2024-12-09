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


def get_space(blocks, indx, is_left):
    val = blocks[indx]
    current = indx
    count = 0

    while current < len(blocks) and current > 0 and val == blocks[current]:
        count += 1

        if is_left:
            current += 1
        else:
            current -= 1

    return count


def sort_blocks(blocks):
    left, right = 0, len(blocks) - 1

    while right > 0:
        if blocks[left] != ".":
            left += 1
            continue

        if blocks[right] == ".":
            right -= 1
            continue

        left_space = get_space(blocks, left, True)
        right_space = get_space(blocks, right, False)

        if left > right:
            current_right_val = blocks[right]
            while right > 0 and blocks[right] == current_right_val:
                right -= 1
            left = 0

            continue

        if left_space >= right_space:
            current_left, current_right = left, right
            left_end, right_end = left + left_space, right - right_space

            while current_left < left_end and current_right > right_end:
                blocks[current_left], blocks[current_right] = (
                    blocks[current_right],
                    blocks[current_left],
                )

                current_left += 1
                current_right -= 1

            left = 0
            right -= right_space

            continue

        left += left_space

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
