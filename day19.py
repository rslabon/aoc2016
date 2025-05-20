class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.next = None
        self.prev = None

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
    nodes = dict()
    i = 1
    while i < 5:
        nodes[current.id] = current
        node = Node(i + 1, 1)
        current.next = node
        node.prev = current
        current = current.next
        i += 1

    nodes[current.id] = current
    current.next = root
    root.prev = current

    current = root
    while current.next != current:
        size = len(nodes)
        opposite_id = current.id + (size // 2)
        opposite_node = nodes[opposite_id]
        current.value += opposite_node.value
        opposite_node.prev.next = opposite_node.next
        current = current.next

    print(current.id, current.value)


# part1()
part2()
