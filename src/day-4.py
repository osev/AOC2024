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


def dfs(board, i, j, word, orientation):
    if len(word) == 0:
        return 1
    if i < 0 or i >= height or j < 0 or j >= width or word[0] != board[i][j]:
        return 0

    tmp = board[i][j]
    board[i][j] = "#"

    sum = 0

    if not orientation:
        sum += dfs(board, i + 1, j, word[1:], "down")
        sum += dfs(board, i - 1, j, word[1:], "up")
        sum += dfs(board, i, j + 1, word[1:], "right")
        sum += dfs(board, i, j - 1, word[1:], "left")
        sum += dfs(board, i + 1, j + 1, word[1:], "down-right")
        sum += dfs(board, i + 1, j - 1, word[1:], "down-left")
        sum += dfs(board, i - 1, j - 1, word[1:], "up-left")
        sum += dfs(board, i - 1, j + 1, word[1:], "up-right")
    else:
        match orientation:
            case "down":
                sum += dfs(board, i + 1, j, word[1:], "down")
            case "up":
                sum += dfs(board, i - 1, j, word[1:], "up")
            case "right":
                sum += dfs(board, i, j + 1, word[1:], "right")
            case "left":
                sum += dfs(board, i, j - 1, word[1:], "left")
            case "down-right":
                sum += dfs(board, i + 1, j + 1, word[1:], "down-right")
            case "down-left":
                sum += dfs(board, i + 1, j - 1, word[1:], "down-left")
            case "up-left":
                sum += dfs(board, i - 1, j - 1, word[1:], "up-left")
            case "up-right":
                sum += dfs(board, i - 1, j + 1, word[1:], "up-right")

    board[i][j] = tmp
    return sum


sum = 0
for x in range(height):
    for y in range(width):
        sum += dfs(parsed, x, y, word, None)

print(sum)
