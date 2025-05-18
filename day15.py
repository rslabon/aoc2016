
def part1():
    original_disc = [
        (5, 17),
        (8, 19),
        (1, 7),
        (7, 13),
        (1, 5),
        (0, 3)
    ]

    for time in range(10000, 100000):
        disc = [] + original_disc
        for index, (current_position, total_positions) in enumerate(disc):
            current_position = (current_position + time + 1 + index) % total_positions
            disc[index] = (current_position, total_positions)

        disc_at_0 = [d for d in disc if d[0] == 0]
        if len(disc_at_0) == len(disc):
            print(time, disc)
            return

def part2():
    original_disc = [
        (5, 17),
        (8, 19),
        (1, 7),
        (7, 13),
        (1, 5),
        (0, 3),
        (0, 11)
    ]

    for time in range(100000, 10000000):
        disc = [] + original_disc
        for index, (current_position, total_positions) in enumerate(disc):
            current_position = (current_position + time + 1 + index) % total_positions
            disc[index] = (current_position, total_positions)

        disc_at_0 = [d for d in disc if d[0] == 0]
        if len(disc_at_0) == len(disc):
            print(time, disc)
            return

part1()
part2()