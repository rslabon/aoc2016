import hashlib


def part1(s):
    index = 0
    password = []
    while len(password) < 8:
        hash = hashlib.md5(f"{s}{index}".encode()).hexdigest()
        if hash[:5] == "00000":
            password.append(hash[5])

        index += 1

    print("".join(password))


def part2(s):
    index = 0
    password = ["#"] * 8
    found = 0
    while found < 8:
        hash = hashlib.md5(f"{s}{index}".encode()).hexdigest()
        if hash[:5] == "00000":
            position = int(hash[5], 16)
            c = hash[6]
            if 0 <= position < 8 and password[position] == "#":
                password[position] = c
                found += 1

        index += 1

    print("".join(password))


part1("ojvtpuvg")
part2("ojvtpuvg")
