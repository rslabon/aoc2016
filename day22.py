import re
from collections import deque

with open("./resources/day22.txt") as f:
    lines = f.read().strip().splitlines()

empty = None
nodes = dict()
for line in lines:
    if line.startswith("/dev/"):
        name, size, used, avail, use = re.split("\s+", line)
        name = name.removeprefix("/dev/grid/node-")
        x, y = re.findall(r"x(\d+)-y(\d+)", name)[0]
        x, y = int(x), int(y)
        nodes[(x, y)] = (int(used[:-1]), int(avail[:-1]), int(size[:-1]), int(use[:-1]))
        if nodes[(x, y)][0] == 0:
            empty = (x, y)


def part1():
    viable_pairs = set()
    for nodeA in nodes.items():
        for nodeB in nodes.items():
            if nodeA != nodeB:
                nodeA_used = nodeA[1][0]
                nodeB_avail = nodeB[1][1]
                if 0 < nodeA_used <= nodeB_avail:
                    viable_pairs.add((nodeA, nodeB))
                    viable_pairs.add((nodeB, nodeA))

    print(len(viable_pairs) // 2)


# part1()

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


q = deque()
target = (30, 0)
_, _, size, _ = nodes[empty]
q.append((empty[0], empty[1], []))
min_steps = float("inf")
seen = set()

while q:
    x, y, path = q.popleft()

    # print("xxxxx", len(path))
    if (x, y) == target:
        if len(path) < min_steps:
            min_steps = len(path)
            print(min_steps)
            for yy in range(0, 31):
                for xx in range(0, 31):
                    used, avail, ssize, use = nodes[(xx, yy)]
                    if (xx, yy) in path:
                        print("0", end="")
                    else:
                        if used <= 92:
                            print(".", end="")
                        else:
                            print("#", end="")
                print("")
            print("")
    else:
        if tuple(path) in seen:
            continue
        seen.add(tuple(path))

        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in path:
                continue
            if not (nx, ny) in nodes:
                continue
            if nodes[(nx, ny)][0] > size:
                continue

            q.append((nx, ny, path + [(x, y)]))

print("xxxxxx", min_steps)
