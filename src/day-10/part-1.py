from collections import defaultdict
from itertools import permutations

test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def parse_input(current_input):
    current_input = current_input.split("\n")
    current_input = [list(row) for row in current_input]
    parsed_input = []
    for row in current_input:
        parsed_input.append([int(val) for val in row])

    return parsed_input


text_file = open("src/day-10/input.txt", "r")
problem_input = text_file.read()

matrix = parse_input(problem_input)
height, width = len(matrix), len(matrix[0])

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


class DFS:
    def __init__(self):
        self.trailhead = set()

    def dfs(self, row, col, prev):
        if col >= width or col < 0 or row >= height or row < 0:
            return 0

        if matrix[row][col] - prev != 1:
            return 0

        if matrix[row][col] == 9:
            return self.trailhead.add((row, col))

        for direction in DIRECTIONS:
            self.dfs(row + direction[0], col + direction[1], matrix[row][col])

        return len(self.trailhead)


paths = 0
for row in range(height):
    for col in range(width):
        if matrix[row][col] == 0:
            dfs = DFS()
            paths += dfs.dfs(row, col, -1)

print(paths)
