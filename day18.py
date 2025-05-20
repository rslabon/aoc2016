from collections import Counter


# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.
def is_trap(row, position):
    pattern = [row[p] if 0 <= p < len(row) else "." for p in [position - 1, position, position + 1]]
    pattern = "".join(pattern)
    if pattern == "^^.":
        return True
    if pattern == ".^^":
        return True
    if pattern == "^..":
        return True
    if pattern == "..^":
        return True

    return False


def next_row(row):
    result = ""
    for i, _ in enumerate(row):
        if is_trap(row, i):
            result += "^"
        else:
            result += "."

    return result


def part1():
    row = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."
    safe_count = 0
    for i in range(40):
        c = Counter(row)
        safe_count += c["."]
        row = next_row(row)

    print(safe_count)


def part2():
    row = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."
    safe_count = 0
    for i in range(400000):
        c = Counter(row)
        safe_count += c["."]
        row = next_row(row)

    print(safe_count)


part1()
part2()
