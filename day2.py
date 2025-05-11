keypad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

keypad2 = [
    ["#", "#", "1", "#", "#"],
    ["#", "2", "3", "4", "#"],
    ["5", "6", "7", "8", "9"],
    ["#", "A", "B", "C", "#"],
    ["#", "#", "D", "#", "#"],
]

instructions = [
    "ULL",
    "RRDDD",
    "LURDL",
    "UUUUD",
]

moves = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}


def press(current, instruction):
    x, y = current
    for i in instruction:
        dx, dy = moves[i]
        x += dx
        x = min(x, len(keypad) - 1)
        x = max(x, 0)
        y += dy
        y = min(y, len(keypad[0]) - 1)
        y = max(y, 0)

    return x, y

def press2(current, instruction):
    x, y = current
    for i in instruction:
        dx, dy = moves[i]
        x += dx
        x = min(x, len(keypad2) - 1)
        x = max(x, 0)
        if keypad2[x][y] == "#":
            x -= dx
        y += dy
        y = min(y, len(keypad2[0]) - 1)
        y = max(y, 0)
        if keypad2[x][y] == "#":
            y -= dy

    return x, y


with open("./resources/day2.txt") as f:
    instructions = f.read().strip().splitlines()


def part1():
    x, y = 1, 1
    pressed = []
    for i in instructions:
        x, y = press((x, y), i)
        pressed.append(keypad[x][y])

    print("".join(pressed))


def part2():
    x, y = 2, 0
    pressed = []
    for i in instructions:
        x, y = press2((x, y), i)
        pressed.append(keypad2[x][y])

    print("".join(pressed))


part1()
part2()
