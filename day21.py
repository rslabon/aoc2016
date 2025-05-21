import re

instructions = [
    "swap position 4 with position 0",
    "swap letter d with letter b",
    "reverse positions 0 through 4",
    "rotate left 1 step",
    "move position 1 to position 4",
    "move position 3 to position 0",
    "rotate based on position of letter b",
    "rotate based on position of letter d"
]
input = "abcde"

# with open("./resources/day21.txt") as f:
#     instructions = f.read().strip().splitlines()
#
# input = "abcdefgh"

input = list(input)


def swap(input, source_index, target_index):
    tmp = input[target_index]
    input[target_index] = input[source_index]
    input[source_index] = tmp
    return input


def reverse_order(input, start, end):
    window = input[start:end + 1]
    window.reverse()
    input = input[0:start] + window + input[end + 1:]
    return input


def rotate_right(input, steps):
    steps = steps % len(input)
    input = input[-steps:] + input[:-steps]
    return input


def rotate_left(input, steps):
    steps = steps % len(input)
    input = input[steps:] + input[:steps]
    return input


def rotate_on_letter(input, letter):
    index = input.index(letter)
    steps = 1 + index
    if index >= 4:
        steps += 1
    input = rotate_right(input, steps)
    return input


def unrotate_on_letter(input, letter):
    index = input.index(letter)
    steps = 1 + index
    if index >= 4:
        steps += 1
    input = rotate_left(input, steps)
    return input


def move(input, source, target):
    letter = input[source]
    del input[source]
    input.insert(target, letter)
    return input


def scramble(input, instructions):
    for instruction in instructions:
        if instruction.startswith("swap position"):
            source, target = re.findall(r"swap position (\d+) with position (\d+)", instruction)[0]
            source, target = int(source), int(target)
            input = swap(input, source, target)
        elif instruction.startswith("swap letter"):
            source, target = re.findall(r"swap letter (\w+) with letter (\w+)", instruction)[0]
            source_indexes = [index for index, c in enumerate(input) if c == source]
            target_indexes = [index for index, c in enumerate(input) if c == target]
            if len(source_indexes) != len(target_indexes):
                raise ValueError("Mismatch indexes!")

            for i, _ in enumerate(source_indexes):
                source_index = source_indexes[i]
                target_index = target_indexes[i]
                input = swap(input, source_index, target_index)
        elif instruction.startswith("reverse positions"):
            start, end = re.findall(r"reverse positions (\d+) through (\d+)", instruction)[0]
            start, end = int(start), int(end)
            input = reverse_order(input, start, end)
        elif instruction.startswith("rotate left"):
            steps, _ = re.findall(r"rotate left (\d+) step(s?)", instruction)[0]
            steps = int(steps)
            input = rotate_left(input, steps)
        elif instruction.startswith("rotate right"):
            steps, _ = re.findall(r"rotate right (\d+) step(s?)", instruction)[0]
            steps = int(steps)
            input = rotate_right(input, steps)
        elif instruction.startswith("rotate based on position of letter"):
            letter = re.findall(r"rotate based on position of letter (\w+)", instruction)[0]
            input = rotate_on_letter(input, letter)
        elif instruction.startswith("move position"):
            source, target = re.findall(r"move position (\d+) to position (\d+)", instruction)[0]
            source, target = int(source), int(target)
            input = move(input, source, target)

        print(instruction, "".join(input))

    return "".join(input)


def unscramble(input, instructions):
    instructions.reverse()
    for instruction in instructions:
        if instruction.startswith("swap position"):
            source, target = re.findall(r"swap position (\d+) with position (\d+)", instruction)[0]
            source, target = int(source), int(target)
            input = swap(input, target, source)
        elif instruction.startswith("swap letter"):
            source, target = re.findall(r"swap letter (\w+) with letter (\w+)", instruction)[0]
            source_indexes = [index for index, c in enumerate(input) if c == source]
            target_indexes = [index for index, c in enumerate(input) if c == target]
            if len(source_indexes) != len(target_indexes):
                raise ValueError("Mismatch indexes!")

            for i, _ in enumerate(source_indexes):
                source_index = source_indexes[i]
                target_index = target_indexes[i]
                input = swap(input, target_index, source_index)
        elif instruction.startswith("reverse positions"):
            start, end = re.findall(r"reverse positions (\d+) through (\d+)", instruction)[0]
            start, end = int(start), int(end)
            input = reverse_order(input, start, end)
        elif instruction.startswith("rotate left"):
            steps, _ = re.findall(r"rotate left (\d+) step(s?)", instruction)[0]
            steps = int(steps)
            input = rotate_right(input, steps)
        elif instruction.startswith("rotate right"):
            steps, _ = re.findall(r"rotate right (\d+) step(s?)", instruction)[0]
            steps = int(steps)
            input = rotate_left(input, steps)
        elif instruction.startswith("rotate based on position of letter"):
            letter = re.findall(r"rotate based on position of letter (\w+)", instruction)[0]
            input = unrotate_on_letter(input, letter)
        elif instruction.startswith("move position"):
            source, target = re.findall(r"move position (\d+) to position (\d+)", instruction)[0]
            source, target = int(source), int(target)
            input = move(input, target, source)

        print(instruction, "".join(input))

    return "".join(input)


def part1():
    print(scramble(input, instructions))


def part2():
    print(scramble(input, instructions))
    print(unscramble(list("decab"), instructions))



# part1()
part2()
