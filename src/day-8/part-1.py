from collections import defaultdict
from itertools import permutations

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


def get_antinode(antennae_a, antennae_b, multiple=1):
    difference = (antennae_b[0] - antennae_a[0], antennae_b[1] - antennae_a[1])
    antinode = (
        antennae_b[0] + (difference[0] * multiple),
        antennae_b[1] + (difference[1] * multiple),
    )

    if (
        antinode[0] >= height
        or antinode[0] < 0
        or antinode[1] >= width
        or antinode[1] < 0
    ):
        return None

    return antinode


antinodes = set()
for freq, indexes in freq_mappings.items():
    for perm in permutations(indexes, 2):
        antinodes.add(get_antinode(perm[0], perm[1]))

print(len(antinodes) - 1)
