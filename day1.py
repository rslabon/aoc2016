moves = ["R5", "L5", "R5", "R3"]


def distance(moves):
    x, y, dir = 0, 0, "N"
    for move in moves:
        turn = move[0]
        steps = int(move[1:])
        if turn == "R":
            if dir == "N":
                dir = "E"
                x += steps
            elif dir == "E":
                dir = "S"
                y += steps
            elif dir == "S":
                dir = "W"
                x -= steps
            else:  # W
                dir = "N"
                y -= steps
        if turn == "L":
            if dir == "N":
                dir = "W"
                x -= steps
            elif dir == "E":
                dir = "N"
                y -= steps
            elif dir == "S":
                dir = "E"
                x += steps
            else:  # W
                dir = "S"
                y += steps

    return abs(x) + abs(y)


def first_visited_twice_distance(moves):
    x, y, dir = 0, 0, "N"
    visited = set()
    visited.add((x, y))

    for move in moves:
        turn = move[0]
        steps = int(move[1:])
        if turn == "R":
            if dir == "N":
                dir = "E"
                for d in range(1, steps + 1):
                    p = (x + d, y)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                x += steps
            elif dir == "E":
                dir = "S"
                for d in range(1, steps + 1):
                    p = (x, y + d)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                y += steps
            elif dir == "S":
                dir = "W"
                for d in range(1, steps + 1):
                    p = (x - d, y)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                x -= steps
            else:  # W
                dir = "N"
                for d in range(1, steps + 1):
                    p = (x, y - d)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                y -= steps
        if turn == "L":
            if dir == "N":
                dir = "W"
                for d in range(1, steps + 1):
                    p = (x - d, y)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                x -= steps
            elif dir == "E":
                dir = "N"
                for d in range(1, steps + 1):
                    p = (x, y - d)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                y -= steps
            elif dir == "S":
                dir = "E"
                for d in range(1, steps + 1):
                    p = (x + d, y)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                x += steps
            else:  # W
                dir = "S"
                for d in range(1, steps + 1):
                    p = (x, y + d)
                    if p in visited:
                        return abs(p[0]) + abs(p[1])
                    visited.add(p)
                y += steps

    raise ValueError("Did not visit any point twice")


def part1():
    with open("./resources/day1.txt") as f:
        moves = f.read().strip().split(", ")
    print(distance(moves))


def part2():
    with open("./resources/day1.txt") as f:
        moves = f.read().strip().split(", ")
    print(first_visited_twice_distance(moves))


part1()
part2()
