test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def parse_input(current_input):
    parsed_first_part = []
    parsed_second_part = []

    first_part, second_part = current_input.split("\n\n")
    first_part = first_part.split("\n")
    for part in first_part:
        x, y = part.split("|")
        parsed_first_part.append([x, y])

    second_part = second_part.split("\n")

    for part in second_part:
        parsed_second_part.append(part.split(","))

    return parsed_first_part, parsed_second_part


text_file = open("src/day-5/input.txt", "r")
problem_input = text_file.read()

first_part, second_part = parse_input(problem_input)

ordering = {}
second_ordering = {}

for part in first_part:
    if part[0] not in second_ordering:
        ordering[part[0]] = []
    if part[0] in second_ordering:
        second_ordering[part[0]].append(part[1])
    else:
        second_ordering[part[0]] = [part[1]]


for part in first_part:
    if part[1] not in ordering:
        ordering[part[0]] = []
    if part[1] in ordering:
        ordering[part[1]].append(part[0])
    else:
        ordering[part[1]] = [part[0]]


def is_valid(part):
    for i in range(len(part) - 1):
        for j in range(i + 1, len(part)):
            if part[j] in ordering[part[i]]:
                return False
    return True


def get_middle(lst):
    if len(lst) % 2 != 0:
        return lst[int(len(lst) / 2)]
    else:
        return ((lst[int(len(lst) / 2)]) + (lst[int(len(lst) / 2) - 1])) / 2


def order(part):
    new_order = []
    for i in range(len(part)):
        element = part[i]

        if len(new_order) == 0:
            new_order.append(element)
        else:
            j = len(new_order) - 1
            while j >= 0:
                if (
                    element in second_ordering
                    and new_order[j] in second_ordering[element]
                ):
                    j -= 1
                else:
                    new_order.insert(j + 1, element)
                    break
            if j == -1:
                new_order.insert(0, element)

    return new_order


sum = 0
for part in second_part:
    if not is_valid(part):
        print("PART IS NOT VALID: ", part)
        new_order = order(part)
        print(new_order)
        sum += int(get_middle(new_order))

print(sum)
