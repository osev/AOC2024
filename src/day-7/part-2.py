test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def parse_input(current_input):
    parsed_input = current_input.split("\n")
    for idx, row in enumerate(parsed_input):
        test, rest = row.split(":")
        parsed_input[idx] = [int(test), rest.strip().split(" ")]
        parsed_input[idx][1] = [int(val) for val in parsed_input[idx][1]]
    return parsed_input


text_file = open("src/day-7/input.txt", "r")
problem_input = text_file.read()


def test_equation(equation, current_sum, target):
    if current_sum == target and not equation:
        return True
    if not equation or current_sum > target:
        return False

    mul_result = equation[0] * current_sum
    mul_valid = test_equation(equation[1:], mul_result, target)

    add_result = equation[0] + current_sum
    add_valid = test_equation(equation[1:], add_result, target)

    or_result = int(str(current_sum) + str(equation[0]))
    or_valid = test_equation(equation[1:], or_result, target)

    return add_valid or mul_valid or or_valid


parsed_input = parse_input(problem_input)
sum = 0

for parsed_equation in parsed_input:
    target_value, equation = parsed_equation
    if test_equation(equation[1:], equation[0], target_value):
        sum += target_value

print(sum)
