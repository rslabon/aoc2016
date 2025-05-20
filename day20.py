with open("./resources/day20.txt") as f:
    lines = f.read().strip().splitlines()

ips = [line.split("-") for line in lines]
ips = [[int(ip[0]), int(ip[1])] for ip in ips]

ips = list(sorted(ips, key=lambda x: x[1]))
ips = list(sorted(ips, key=lambda x: x[0]))


def part1():
    merged = [ips[0]]
    i = 0
    while i < len(ips):
        prev = merged[-1]
        current = ips[i]
        if prev[1] >= current[0]:
            prev[1] = max(prev[1], current[1])
        if not (prev[1] >= current[0] or prev[1] >= current[1]):
            merged.append(current)
        i += 1

    i = 1
    allowed_ips = []
    while i < len(merged):
        prev = merged[i - 1]
        current = merged[i]
        if prev[1] + 1 < current[0]:
            allowed_ips.append((prev[1] + 1, current[0] - 1))
        i += 1

    print(allowed_ips[0][0])


def part2():
    merged = [ips[0]]
    i = 0
    while i < len(ips):
        prev = merged[-1]
        current = ips[i]
        if prev[1] >= current[0]:
            prev[1] = max(prev[1], current[1])
        if not (prev[1] >= current[0] or prev[1] >= current[1]):
            merged.append(current)
        i += 1

    i = 1
    allowed_ips = []
    max_blocked_ip = -1
    while i < len(merged):
        prev = merged[i - 1]
        current = merged[i]
        if prev[1] + 1 < current[0]:
            allowed_ips.append((prev[1] + 1, current[0] - 1))
        i += 1
        max_blocked_ip = max(max_blocked_ip, current[1], prev[1])

    total = 4294967295 - max_blocked_ip
    for start, end in allowed_ips:
        total += 1 + end - start

    print(total)


part1()
part2()

