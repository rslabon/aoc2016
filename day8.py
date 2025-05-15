width = 7
height = 3

commands = [
    "rect 3x2",
    "rotate column x=1 by 1",
    "rotate row y=1 by 1",
    "rotate column x=1 by 1",
]

width = 50
height = 6

with open("./resources/day8.txt") as f:
    commands = f.read().strip().splitlines()

grid = []
for row in range(height):
    grid.append([])
    for _ in range(width):
        grid[row].append(".")


def printGrid():
    for row in range(height):
        for col in range(width):
            print(grid[row][col], end="")
        print()
    print()


def rect(a, b):
    for row in range(b):
        for col in range(a):
            grid[row][col] = "#"


def rotate_column(a, b):
    if b == 0:
        return

    row = 0
    prev = grid[row - 1][a]
    while row < height:
        current = grid[row][a]
        grid[row][a] = prev
        prev = current
        row += 1

    rotate_column(a, b - 1)


def rotate_row(a, b):
    if b == 0:
        return

    col = 0
    prev = grid[a][col - 1]
    while col < width:
        current = grid[a][col]
        grid[a][col] = prev
        prev = current
        col += 1

    rotate_row(a, b - 1)


def execute(command):
    # rect AxB
    if command.startswith("rect"):
        _, size = command.split(" ")
        a, b = map(int, size.split("x"))
        rect(a, b)

    # rotate column x=A by B
    if command.startswith("rotate column"):
        command = command.removeprefix("rotate column x=")
        a, b = map(int, command.split(" by "))
        rotate_column(a, b)

    # rotate row y=A by B
    if command.startswith("rotate row"):
        command = command.removeprefix("rotate row y=")
        a, b = map(int, command.split(" by "))
        rotate_row(a, b)


def count_lit():
    count = 0
    for row in range(height):
        for col in range(width):
            if grid[row][col] == "#":
                count += 1
    return count


def part1():
    for command in commands:
        execute(command)

    print(count_lit())

def part2():
    for command in commands:
        execute(command)

    printGrid() # ZJHRKCPLYJ


part1()
part2()
