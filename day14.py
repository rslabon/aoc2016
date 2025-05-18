import hashlib


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()


def stretche(hash):
    i = 0
    while i <= 2016:
        hash = md5(hash)
        i += 1

    return hash


def contains_window(s, size):
    start = 0
    end = size
    while end <= len(s):
        window = s[start:end]
        if len(set(window)) == 1:
            return window[0]

        start += 1
        end += 1

    return None


def find_64key(salt, use_stretche=False):
    i = 0
    triplets = []
    keys = []
    while len(keys) < 64:
        if use_stretche:
            h = stretche(f"{salt}{i}")
        else:
            h = md5(f"{salt}{i}")
        t3 = contains_window(h, 3)
        t5 = contains_window(h, 5)
        if t5:
            potential_keys = [t3[0] for t3 in triplets if i - 1000 <= t3[0] < i and t3[1] == t5]
            for k in potential_keys:
                if k not in keys:
                    keys.append(k)

            triplets.append((i, t5))
        if t3:
            triplets.append((i, t3))

        i += 1

    print(sorted(keys)[:64][-1])


def part1():
    salt = "abc"
    salt = "yjdafjpo"
    find_64key(salt, use_stretche=False)


def part2():
    salt = "abc"
    salt = "yjdafjpo"
    find_64key(salt, use_stretche=True)


part1()
part2()
