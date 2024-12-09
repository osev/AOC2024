import os

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

text_file = open("src/day-4.txt", "r")
problem_input = text_file.read()

word = "XMAS"


def parse_input(current_input):
    lines = current_input.split("\n")
    matrix = []
    for line in lines:
        matrix.append(list(line))

    return matrix


parsed = parse_input(problem_input)
print(parsed)
height = len(parsed)
width = len(parsed[0])


def dfs(board, i, j):
    print("middle letter: ", board[i][j])
    if i - 1 < 0 or i + 1 >= height or j - 1 < 0 or j + 1 >= width:
        return False

    if not (
        (board[i - 1][j - 1] == "M" and board[i + 1][j + 1] == "S")
        or (board[i - 1][j - 1] == "S" and board[i + 1][j + 1] == "M")
    ):
        letters = (board[i - 1][j - 1], board[i + 1][j + 1])
        print(letters)
        print("Could not find on diag 1")
        return False
    if not (
        (board[i - 1][j + 1] == "M" and board[i + 1][j - 1] == "S")
        or (board[i - 1][j + 1] == "S" and board[i + 1][j - 1] == "M")
    ):
        letters = (board[i - 1][j + 1], board[i - 1][j + 1])
        print(letters)
        print("Could not find on diag 2")
        return False

    return True


sum = 0

for x in range(height):
    for y in range(width):
        if parsed[x][y] == "A":
            is_match = dfs(parsed, x, y)
            if is_match:
                sum += 1


print(sum)
