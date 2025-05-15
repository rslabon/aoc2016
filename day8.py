commands = [
    "rect 3x2",
    "rotate column x=1 by 1",
    "rotate row y=1 by 1",
    "rotate column x=1 by 1",
]

with open("./resources/day8.txt") as f:
    commands = f.read().strip().splitlines()


def create_grid(width, height):
    grid = []
    for row in range(height):
        grid.append([])
        for _ in range(width):
            grid[row].append(".")

    return grid


def printGrid(grid):
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            print(grid[row][col], end="")
        print()

    print()


def rect(grid, a, b):
    for row in range(b):
        for col in range(a):
            grid[row][col] = "#"


def rotate_column(grid, a, b):
    if b == 0:
        return

    height = len(grid)
    row = 0
    prev = grid[row - 1][a]
    while row < height:
        current = grid[row][a]
        grid[row][a] = prev
        prev = current
        row += 1

    rotate_column(grid, a, b - 1)


def rotate_row(grid, a, b):
    if b == 0:
        return

    width = len(grid[0])
    col = 0
    prev = grid[a][col - 1]
    while col < width:
        current = grid[a][col]
        grid[a][col] = prev
        prev = current
        col += 1

    rotate_row(grid, a, b - 1)


def execute(grid, command):
    # rect AxB
    if command.startswith("rect"):
        _, size = command.split(" ")
        a, b = map(int, size.split("x"))
        rect(grid, a, b)

    # rotate column x=A by B
    if command.startswith("rotate column"):
        command = command.removeprefix("rotate column x=")
        a, b = map(int, command.split(" by "))
        rotate_column(grid, a, b)

    # rotate row y=A by B
    if command.startswith("rotate row"):
        command = command.removeprefix("rotate row y=")
        a, b = map(int, command.split(" by "))
        rotate_row(grid, a, b)


def count_lit(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            if grid[row][col] == "#":
                count += 1
    return count


def part1():
    grid = create_grid(50, 6)
    for command in commands:
        execute(grid, command)

    print(count_lit(grid))


def part2():
    grid = create_grid(50, 6)
    for command in commands:
        execute(grid, command)

    printGrid(grid)  # ZJHRKCPLYJ


part1()
part2()
