moves = ["R5", "L5", "R5", "R3"]

dirs = [
    (-1, 0),  # N
    (0, 1),  # E
    (1, 0),  # S
    (0, -1),  # W
]


def distance(moves):
    x, y, dir = 0, 0, 0
    for move in moves:
        turn = move[0]
        steps = int(move[1:])
        dir = (dir + 1) % 4 if turn == "R" else (dir - 1) % 4
        dx, dy = dirs[dir]
        x += dx * steps
        y += dy * steps

    return abs(x) + abs(y)


def first_visited_twice_distance(moves):
    x, y, dir = 0, 0, 0
    visited = set()
    visited.add((0, 0))
    for move in moves:
        turn = move[0]
        steps = int(move[1:])
        dir = (dir + 1) % 4 if turn == "R" else (dir - 1) % 4
        dx, dy = dirs[dir]
        for step in range(1, steps + 1):
            x += dx
            y += dy
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    raise ValueError("ERROR!")


with open("./resources/day1.txt") as f:
    moves = f.read().strip().split(", ")


def part1():
    print(distance(moves))


def part2():
    print(first_visited_twice_distance(moves))


part1()
part2()
