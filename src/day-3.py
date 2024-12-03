import re
import os

test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))"

sum = 0

text_file = open("src/day-3.txt", "r")
problem_input = text_file.read()

matches = re.findall(pattern, problem_input)


def parse_mult(instruction):
    numbers = instruction.replace("mul(", "").replace(")", "")
    x, y = numbers.split(",")
    mult = int(x) * int(y)
    return mult


enabled = True
sum = 0

for match in matches:
    instruction = ""

    for m in match:
        instruction += m

    if instruction.startswith("mul"):
        if enabled:
            sum += parse_mult(instruction)

    if instruction.startswith("don"):
        enabled = False

    if instruction.startswith("do()"):
        enabled = True

    print(instruction)


print(sum)
