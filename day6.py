from collections import Counter

input = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""

messages = input.strip().splitlines()

with open("./resources/day6.txt", "r") as f:
    messages = f.read().strip().splitlines()


def part1():
    column_values = []
    for _ in range(len(messages[0])):
        column_values.append("")

    for row, message in enumerate(messages):
        for column, letter in enumerate(message):
            column_values[column] += letter

    correction = [Counter(value).most_common()[0][0] for value in column_values]
    print("".join(correction))


def part2():
    column_values = []
    for _ in range(len(messages[0])):
        column_values.append("")

    for row, message in enumerate(messages):
        for column, letter in enumerate(message):
            column_values[column] += letter

    correction = [Counter(value).most_common()[-1][0] for value in column_values]
    print("".join(correction))


part1()
part2()
