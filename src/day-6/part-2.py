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


guard_i, guard_j, guard = find_guard(parsed_input)


def contains_loop(matrix):
    areas = set()

    i, j, guard = find_guard(parsed_input)
    areas.add((i, j, guard))

    while next_step(matrix, i, j, guard):
        i, j, guard = next_step(matrix, i, j, guard)

        new_pos = (i, j, guard)

        if new_pos in areas:
            return 1

        areas.add((i, j, guard))

    return 0


num_obstacles = 0

for i in range(height):
    for j in range(width):
        if parsed_input[i][j] == ".":
            if i == guard_i and j == guard_j:
                continue
            parsed_input[i][j] = "#"
            num_obstacles += contains_loop(parsed_input)
            parsed_input[i][j] = "."


print(num_obstacles)
