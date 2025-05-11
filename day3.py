import re

with open("./resources/day3.txt") as f:
    lines = f.read().strip().splitlines()


def is_triangle(numbers):
    numbers.sort()
    v1, v2, v3 = numbers
    if v1 + v2 > v3:
        return 1
    return 0


def parse_data():
    data = []
    for line in lines:
        numbers = re.findall(r"\d+", line)
        numbers = [int(n) for n in numbers]
        data.append(numbers)

    return data


def part1():
    count = 0
    data = parse_data()
    for i in data:
        count += is_triangle(i)

    print(count)


def part2():
    count = 0
    data = parse_data()

    for i in range(0, len(data), 3):
        count += is_triangle([data[i][0], data[i + 1][0], data[i + 2][0]])
        count += is_triangle([data[i][1], data[i + 1][1], data[i + 2][1]])
        count += is_triangle([data[i][2], data[i + 1][2], data[i + 2][2]])

    print(count)


part1()
part2()
