from collections import Counter

alphabet = ["a", "b", "c", "d", "e",
            "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y",
            "z"]

index = dict()
for i, c in enumerate(alphabet):
    index[c] = i


def real_room_sector_id(s):
    parts = s.strip().split("-")
    sector_id, checksum = parts[-1].split("[")
    checksum = checksum[:-1]
    parts = parts[:-1]
    actual_checksum = list(sorted(Counter("".join(parts)).items(), key=lambda i: i[0]))
    actual_checksum = list(sorted(actual_checksum, key=lambda i: i[1], reverse=True))
    actual_checksum = [i[0] for i in actual_checksum]
    actual_checksum = "".join(actual_checksum)[:5]
    if actual_checksum == checksum:
        return int(sector_id)

    return 0


with open("./resources/day4.txt") as f:
    lines = f.read().strip().splitlines()


def part1():
    count = 0
    for line in lines:
        count += real_room_sector_id(line)

    print(count)


def decrypt_name(s):
    parts = s.strip().split("-")
    sector_id, _ = parts[-1].split("[")
    sector_id = int(sector_id)
    parts = parts[:-1]
    name = []
    for part in parts:
        decrypted_part = ""
        for c in part:
            shifted = (index[c] + sector_id) % len(alphabet)
            decrypted_part += alphabet[shifted]
        name.append(decrypted_part)

    return " ".join(name), sector_id


def part2():
    for line in lines:
        name, sector_id = decrypt_name(line)
        if name == "northpole object storage":
            print(sector_id)
            break


part1()
part2()
