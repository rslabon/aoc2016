import functools
from collections import deque

data = [
    "ADVENT",
    "A(1x5)BC",
    "(3x3)XYZ",
    "A(2x2)BCD(2x2)EFG",
    "(6x1)(1x3)A",
    "X(8x2)(3x3)ABCY",
]


@functools.cache
def decompress_length(s, nested=False):
    buffor = ""
    result = 0

    a = ""
    b = ""
    q = deque(s)
    while q:
        c = str(q.popleft())
        if c == ")":
            b = buffor
            length = int(a)
            repeat = int(b)
            a = ""
            b = ""
            i = 0
            buffor = ""
            while q and i < length:
                buffor += str(q.popleft())
                i += 1
            if nested:
                result += decompress_length(buffor * repeat, nested)
            else:
                result += len(buffor) * repeat
        elif c == "x":
            a = str(buffor)
            buffor = ""
        elif c == "(":
            buffor = ""
            a = ""
            b = ""
        elif c.isdigit():
            buffor += c
        else:
            result += 1

    return result


def part1():
    with open("./resources/day9.txt") as f:
        s = f.read().strip().splitlines()[0]
        print(decompress_length(s))


def part2():
    with open("./resources/day9.txt") as f:
        s = f.read().strip().splitlines()[0]
        print(decompress_length(s, True))


part1()
part2()
