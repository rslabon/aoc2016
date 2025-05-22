import re

with open("./resources/day22.txt") as f:
    lines = f.read().strip().splitlines()

empty = None
nodes = dict()
for line in lines:
    if line.startswith("/dev/"):
        name, size, used, avail, use = re.split(r"\s+", line)
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


part1()
# part2 printed nodes and computed on paper
