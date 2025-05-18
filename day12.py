instructions = """
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""

with open("./resources/day12.txt", "r") as f:
    instructions = f.read()

instructions = instructions.strip().splitlines()

def execute(instructions, registers):
    index = 0
    while index < len(instructions):
        instruction = instructions[index].split(" ")
        if instruction[0] == 'cpy':
            if instruction[1].isdigit():
                registers[instruction[2]] = int(instruction[1])
            else:
                registers[instruction[2]] = registers[instruction[1]]
            index += 1
        if instruction[0] == 'inc':
            registers[instruction[1]] += 1
            index += 1
        if instruction[0] == 'dec':
            registers[instruction[1]] -= 1
            index += 1
        if instruction[0] == 'jnz':
            if instruction[1].isdigit():
                if int(instruction[1]) != 0:
                    index += int(instruction[2])
                else:
                    index += 1
            else:
                if registers[instruction[1]] != 0:
                    index += int(instruction[2])
                else:
                    index += 1

    print(registers["a"])

def part1():
    registers = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    execute(instructions, registers)

def part2():
    registers = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0,
    }
    execute(instructions, registers)

part1()
part2()