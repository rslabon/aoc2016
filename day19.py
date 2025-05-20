class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.next = None

    def __repr__(self):
        return f"#{self.id} [{self.value}]"


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
    root = Node(1, 1)
    current = root
    i = 1
    size = 3014387
    before_opposite_node = None
    while i < size:
        node = Node(i + 1, 1)
        current.next = node
        current = current.next
        if i == (size // 2) - 1:
            before_opposite_node = node
        i += 1

    current.next = root

    current = root
    while current.next != current:
        if size <= 3:
            before_opposite_node = current
            opposite_node = current.next
        else:
            opposite_node = before_opposite_node.next

        current.value += opposite_node.value
        before_opposite_node.next = opposite_node.next

        if size % 2 == 1:
            before_opposite_node = before_opposite_node.next

        current = current.next
        size -= 1

    print(current.id)


part1()
part2()
