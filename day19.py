class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.next = None


def part1():
    root = Node(1, 1)
    current = root
    i = 1
    while i < 3014387:
        current.next = Node(i + 1, 1)
        current = current.next
        i += 1
    current.next = root

    current = root
    while current.next != current:
        current.value += current.next.value
        current.next = current.next.next
        current = current.next

    print(current.id)


def part2():
    elfs = dict()
    i = 1
    while i <= 5:
        elfs[i] = 1
        i += 1

    current = 1
    while len(elfs) > 1:
        size = len(elfs)
        if size % 2 == 0:
            size += 1
        i = current + (size // 2)
        elfs[current] += elfs[i]
        del elfs[i]
        current = (current + 1) % (1 + len(elfs))
        while current not in elfs:
            current = (current + 1) % (1 + len(elfs))

    print(elfs)


# part1()
part2()
