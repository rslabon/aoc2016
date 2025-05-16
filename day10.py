import re

instructions = [
    "value 5 goes to bot 2",
    "bot 2 gives low to bot 1 and high to bot 0",
    "value 3 goes to bot 1",
    "bot 1 gives low to output 1 and high to bot 0",
    "bot 0 gives low to output 2 and high to output 0",
    "value 2 goes to bot 2",
]

with open("./resources/day10.txt") as f:
    instructions = f.read().strip().splitlines()


def parse():
    bots = dict()
    values = dict()

    init_instructions = [inst for inst in instructions if inst.startswith("value")]
    for inst in init_instructions:
        value, bot = re.findall(r"value (\d+) goes to (bot \d+)", inst)[0]
        value = int(value)
        v = values.get(bot, [])
        v.append(value)
        values[bot] = v

    rest_instructions = [inst for inst in instructions if inst.startswith("bot")]
    for inst in rest_instructions:
        from_bot, low_target, high_target = \
            re.findall(r"(bot \d+) gives low to (output \d+|bot \d+) and high to (output \d+|bot \d+)", inst)[0]
        bots[from_bot] = (low_target, high_target)

    return bots, values


def part1():
    bots, values = parse()

    found = False
    while not found:
        ready_bots = [(bot, vals) for bot, vals in values.items() if len(vals) == 2]
        for bot, vals in ready_bots:
            low_value, high_value = sorted(vals)
            low_target, high_target = bots[bot]
            v = values.get(low_target, [])
            v.append(low_value)
            values[low_target] = v

            v = values.get(high_target, [])
            v.append(high_value)
            values[high_target] = v

            values[bot] = []

            if low_value == 17 and high_value == 61:
                print(str(bot).removeprefix("bot "))
                found = True
                break


def part2():
    bots, values = parse()
    while not ("output 0" in values and "output 1" in values and "output 2" in values):
        ready_bots = [(bot, vals) for bot, vals in values.items() if len(vals) == 2]
        for bot, vals in ready_bots:
            low_value, high_value = sorted(vals)
            low_target, high_target = bots[bot]
            v = values.get(low_target, [])
            v.append(low_value)
            values[low_target] = v

            v = values.get(high_target, [])
            v.append(high_value)
            values[high_target] = v

            values[bot] = []

    print(values["output 0"][0] * values["output 1"][0] * values["output 2"][0])


part1()
part2()
