from collections import Counter
from collections import deque


def bin_string(n):
    return bin(n)[2:]


def cell(x, y, favorite_number):
    formula = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    formula += favorite_number
    c = Counter(bin_string(formula))
    if c["1"] % 2 == 0:
        return "."
    else:
        return "#"


def create_grid(height, width, favorite_number):
    grid = dict()
    for y in range(width):
        for x in range(height):
            grid[(x, y)] = cell(x, y, favorite_number)

    return grid


def part1():
    height = 40
    width = 40
    favorite_number = 1362
    grid = create_grid(height, width, favorite_number)

    q = deque()
    q.append((1, 1, []))
    min_steps = float("inf")
    target = (31, 39)

    while q:
        x, y, path = q.popleft()
        if (x, y) in path:
            continue

        if (x, y) == target:
            path = path + [(x, y)]
            if len(path) < min_steps:
                min_steps = len(path)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if (nx, ny) not in grid:
                continue
            if grid[(nx, ny)] == "#":
                continue
            q.append((nx, ny, path + [(x, y)]))

    print(min_steps - 1)


def part2():
    height = 40
    width = 40
    favorite_number = 1362
    grid = create_grid(height, width, favorite_number)

    q = deque()
    q.append((1, 1, []))
    seen = set()

    while q:
        x, y, path = q.popleft()
        if (x, y) in path:
            continue

        if len(path) > 50:
            continue

        seen.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if (nx, ny) not in grid:
                continue
            if grid[(nx, ny)] == "#":
                continue
            q.append((nx, ny, path + [(x, y)]))

    print(len(seen))


# part1()
part2()
