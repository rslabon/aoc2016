import functools
from collections import deque


def step(s):
    a = s
    b = a
    b = b[::-1]
    b = "".join(["1" if i == "0" else "0" for i in b])
    return f"{a}0{b}"


def filup(s, size):
    while len(s) < size:
        s = step(s)
    return s[:size]


@functools.cache
def checksum(s):
    if len(s) % 2 == 1:
        raise ValueError("checksum only works for odd sized strings")

    q = deque(s)
    result = ""
    while q:
        a = q.popleft()
        b = q.popleft()
        if a == b:
            result += "1"
        else:
            result += "0"

    if len(result) % 2 == 0:
        return checksum(result)
    else:
        return result


def part1():
    state = "10010000000110000"
    state = filup(state, 272)
    print(checksum(state))


def part2():
    state = "10010000000110000"
    state = filup(state, 35651584)
    print(checksum(state))


part1()
part2()
