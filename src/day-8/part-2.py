from collections import defaultdict
from itertools import permutations
from math import gcd

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def parse_input(current_input):
    parsed_input = current_input.split("\n")
    parsed_input = [list(row) for row in parsed_input]
    return parsed_input


text_file = open("src/day-8/input.txt", "r")
problem_input = text_file.read()
matrix = parse_input(problem_input)
height, width = len(matrix), len(matrix[0])


def get_freq_mappings(matrix):
    freq_dict = defaultdict(set)

    for i in range(height):
        for j in range(width):
            freq = matrix[i][j]
            if freq != ".":
                freq_dict[freq].add((i, j))

    return freq_dict


sum = 0
freq_mappings = get_freq_mappings(matrix)


def is_valid(current_antennae):
    return 0 <= current_antennae[0] < height and 0 <= current_antennae[1] < width


def get_antinodes(antennae_a, antennae_b):
    dx = antennae_b[0] - antennae_a[0]
    dy = antennae_b[1] - antennae_a[1]

    divisor = gcd(dx, dy)
    step_x = dx // divisor
    step_y = dy // divisor

    antinodes = set()
    current = antennae_b

    while is_valid(current):
        antinodes.add(current)
        current = (current[0] + step_x, current[1] + step_y)

    return antinodes


antinodes = set()
for freq, indexes in freq_mappings.items():
    for perm in permutations(indexes, 2):
        antinodes.update(get_antinodes(perm[0], perm[1]))

print(len(antinodes))
