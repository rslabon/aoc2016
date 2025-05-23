instructions = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""

with open("./resources/day23.txt", "r") as f:
    instructions = f.read()

instructions = instructions.strip().splitlines()


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def toggle_instruction(index, instructions):
    if index > len(instructions) - 1:
        return
    parts = instructions[index].split(" ")
    name = parts[0]
    arguments = parts[1:]
    if len(arguments) == 1:
        if name == "inc":
            name = "dec"
        else:
            name = "inc"
    elif len(arguments) == 2:
        if name == "jnz":
            name = "cpy"
        else:
            name = "jnz"

    instructions[index] = name + " " + " ".join(arguments)


def execute(instructions, registers):
    index = 0
    while index < len(instructions):
        instruction = instructions[index].split(" ")
        if instruction[0] == "tgl":
            if not is_number(instructions[1]):
                x = registers[instruction[1]]
                toggle_instruction(index + x, instructions)
            index += 1
        if instruction[0] == 'cpy':
            if not is_number(instruction[2]):
                if index + 6 < len(instructions):
                    block = instructions[index:index + 6]
                    # pattern based on puzzle input: a += d*b, d=0, c=0
                    pattern = [
                        "cpy b c",
                        "inc a",
                        "dec c",
                        "jnz c -2",
                        "dec d",
                        "jnz d -5",
                    ]
                    if block == pattern:
                        registers["a"] += registers["d"] * registers["b"]
                        registers["c"] = 0
                        registers["d"] = 0
                        index += 6
                    elif is_number(instruction[1]):
                        registers[instruction[2]] = int(instruction[1])
                        index += 1
                    else:
                        registers[instruction[2]] = registers[instruction[1]]
                        index += 1
                else:
                    if is_number(instruction[1]):
                        registers[instruction[2]] = int(instruction[1])
                    else:
                        registers[instruction[2]] = registers[instruction[1]]
                    index += 1
        if instruction[0] == 'inc':
            if not is_number(instructions[1]):
                registers[instruction[1]] += 1
            index += 1
        if instruction[0] == 'dec':
            if not is_number(instructions[1]):
                registers[instruction[1]] -= 1
            index += 1
        if instruction[0] == 'jnz':
            if is_number(instruction[1]):
                x = int(instruction[1])
            else:
                x = registers[instruction[1]]

            if is_number(instruction[2]):
                y = int(instruction[2])
            else:
                y = registers[instruction[2]]

            if x != 0:
                index += y
            else:
                index += 1

    print(registers["a"])


def part1():
    registers = {
        "a": 7,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    execute([] + instructions, registers)


def part2():
    registers = {
        "a": 12,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    execute([] + instructions, registers)


part1()
part2()
