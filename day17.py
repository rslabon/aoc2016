import hashlib
from collections import deque

open = {"b", "c", "d", "e", "f"}

height = 4
width = 4


def adj(passcode):
    s = hashlib.md5(passcode.encode()).hexdigest()[:4]
    up, down, left, right = s
    result = []
    if up in open:
        result.append((-1, 0, "U"))
    if down in open:
        result.append((1, 0, "D"))
    if left in open:
        result.append((0, -1, "L"))
    if right in open:
        result.append((0, 1, "R"))

    return result


def part1():
    original_passcode = "vkjiggvb"
    q = deque()
    q.append((0, 0, original_passcode, []))
    target = (height - 1, width - 1)
    min_path = float("inf")
    min_moves = None

    while q:
        x, y, passcode, path = q.popleft()

        if len(path) > min_path:
            continue

        if (x, y) == target:
            if min_path > len(path):
                min_path = len(path)
                min_moves = passcode.replace(original_passcode, "")

        for dx, dy, move in adj(passcode):
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < height and 0 <= ny < width):
                continue
            q.append((nx, ny, passcode + move, path + [(x, y)]))

    print(min_moves)


def part2():
    original_passcode = "vkjiggvb"
    q = deque()
    q.append((0, 0, original_passcode, []))
    target = (height - 1, width - 1)
    max_steps = -1

    while q:
        x, y, passcode, path = q.popleft()

        if (x, y) == target:
            max_steps = max(len(path), max_steps)
        else:
            for dx, dy, move in adj(passcode):
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < height and 0 <= ny < width):
                    continue
                npath = path + [(x, y)]
                q.append((nx, ny, passcode + move, npath))

    print(max_steps)


part1()
part2()
