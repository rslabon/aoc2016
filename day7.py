ips = [
    "abba[mnop]qrst",
    "abcd[bddb]xyyx",
    "aaaa[qwer]tyui",
    "ioxxoj[asdfgh]zxcvbn",
]

ips = [
    "aba[bab]xyz",
    "xyx[xyx]xyx",
    "aaa[kek]eke",
    "zazbz[bzb]cdb",
]

with open("./resources/day7.txt") as f:
    ips = f.read().strip().splitlines()


def is_abba(s):
    start = 0
    end = 4
    while end <= len(s):
        window = s[start:end]
        if window[0] == window[3] and window[1] == window[2] and window[0] != window[1]:
            return True
        start += 1
        end += 1

    return False


def find_aba(s):
    start = 0
    end = 3
    found = []
    while end <= len(s):
        window = s[start:end]
        if window[0] == window[2] and window[0] != window[1]:
            found.append(window)
        start += 1
        end += 1

    return found


def parse(s):
    outside = []
    inside = []
    current = ""
    for c in s:
        if c == "[":
            outside.append(current)
            current = ""
        elif c == "]":
            inside.append(current)
            current = ""
        else:
            current += c

    if current:
        outside.append(current)

    return outside, inside


data = []
for ip in ips:
    data.append(parse(ip))


def has_ttl(outside, inside):
    found = 0
    for s in outside:
        if is_abba(s):
            found = 1

    for s in inside:
        if is_abba(s):
            found = 0

    return found == 1


def part1():
    count = 0
    for outside, inside in data:
        if has_ttl(outside, inside):
            count += 1

    print(count)


def has_ssl(outside, inside):
    outside_aba = set()
    for out in outside:
        outside_aba |= set(find_aba(out))

    inside_bab = set()
    for ins in inside:
        inside_bab |= set(find_aba(ins))

    inside_aba = set([f"{bab[1]}{bab[0]}{bab[1]}" for bab in inside_bab])

    return outside_aba & inside_aba


def part2():
    count = 0
    for outside, inside in data:
        if has_ssl(outside, inside):
            count += 1

    print(count)


part1()
part2()
