test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

guard_direction = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

guard_next_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}


def parse_input(current_input):
    parsed_input = current_input.split("\n")
    for idx, row in enumerate(parsed_input):
        parsed_input[idx] = list(row)

    return parsed_input


text_file = open("src/day-6/input.txt", "r")
problem_input = text_file.read()

parsed_input = parse_input(problem_input)
height, width = len(parsed_input), len(parsed_input[0])


def find_guard(matrix):
    for i in range(height):
        for j in range(width):
            if matrix[i][j] in guard_direction:
                return i, j, matrix[i][j]


def next_step(matrix, i, j, guard):
    next_i, next_j = guard_direction[guard]

    calculated_i = i + next_i
    calculated_j = j + next_j

    ## Out of bounds
    if (
        calculated_i < 0
        or calculated_i >= height
        or calculated_j < 0
        or calculated_j >= width
    ):
        return False

    if matrix[calculated_i][calculated_j] == "#":
        # Turn around
        guard = guard_next_direction[guard]
        return next_step(matrix, i, j, guard)

    return calculated_i, calculated_j, guard


i, j, guard = find_guard(parsed_input)
areas = set()
areas.add((i, j))

while next_step(parsed_input, i, j, guard):
    i, j, guard = next_step(parsed_input, i, j, guard)
    areas.add((i, j))

print(len(areas))
