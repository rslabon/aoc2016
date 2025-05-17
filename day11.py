import functools
import heapq
import itertools
import re

# example
floors = """
4 .  .  .  .  .
3 .  .  .  LG .
2 .  HG .  .  .
1 E  .  HM .  LM
"""

# part1
floors = """
4 .  .  .  .  .  .  .  .  .  .  .
3 .  .  .  .  .  .  .  PRM PRG RM RG
2 .  .  .  PLM .  SM .  .  .  .  .
1 E  TM TG .  PLG .  SG .  .  .  .
"""

# part2
floors = """
4 .  .  .  .  .   .   .   .   .   .  .  .  .  .  .
3 .  .  .  .  .   .   .   PRM PRG RM RG .  .  .  .
2 .  .  .  PLM .  SM  .   .   .   .  .  .  .  .  .
1 E  TM TG .  PLG .   SG  .   .   .  .  EG EM DG DM
"""


def create_grid():
    grid = []
    for row, floor in enumerate(floors.strip().splitlines()):
        grid.append([])
        for val in re.split(r"\s+", floor):
            grid[row].append(val)

    return grid


def printGrid(grid):
    for row in grid:
        for val in row:
            print(f"{val:3}", end=" ")
        print()
    print()


def is_safe(items):
    generators = [n[:-1] for n in items if str(n)[-1] == "G"]
    chips = [n[:-1] for n in items if str(n)[-1] == "M"]
    generators_without_chips = set(generators) - set(chips)
    chips_without_generators = set(chips) - set(generators)
    if len(generators_without_chips) == 0 or len(chips_without_generators) == 0:
        return True

    return not (len(chips_without_generators) >= 1 and len(chips_without_generators) >= 1)


def items_on_floor(grid, floor_nr):
    return set([item for item in grid[len(grid) - floor_nr] if item[-1] == "G" or item[-1] == "M"])


def can_move_to(grid, names, floor_nr):
    destination = items_on_floor(grid, floor_nr) | set(names)
    return is_safe(destination)


def can_move_from(grid, names, floor_nr):
    destination = items_on_floor(grid, floor_nr) - set(names)
    return is_safe(destination)


def can_move_from_to(grid, names, from_floor, to_floor):
    return can_move_from(grid, names, from_floor) and can_move_to(grid, names, to_floor)


def deep_copy(grid):
    new_grid = []
    for row in grid:
        new_grid.append([])
        for val in row:
            new_grid[-1].append(val)

    return new_grid


def to_string(grid):
    s = ""
    for row in grid:
        for val in row:
            s += f"{val:4}"
        s += "\n"

    return s


def parse(s):
    rows = s.splitlines()
    grid = []
    for row in rows:
        grid.append([])
        for val in re.split(r"\s+", row):
            if val:
                grid[-1].append(val)

    return grid


@functools.cache
def move(string_grid, names, from_floor, to_floor):
    grid = parse(string_grid)
    if not can_move_from_to(grid, names, from_floor, to_floor):
        return False, to_string(grid)

    for col, name in enumerate(grid[len(grid) - from_floor]):
        if name in names:
            grid[len(grid) - to_floor][col] = name
            grid[len(grid) - from_floor][col] = "."
            grid[len(grid) - to_floor][1] = "E"
            grid[len(grid) - from_floor][1] = "."

    return True, to_string(grid)


def possible_items_to_move(grid, floor_nr):
    items = set(items_on_floor(grid, floor_nr))

    possible = set()
    for a, b in itertools.combinations(items, 2):
        if (a[-1] == "G" and b[-1] == "M" or a[-1] == "M" and b[-1] == "G") and a[0:-1] == b[0:-1]:
            possible.add(frozenset({a, b}))
        elif a[-1] == b[-1]:
            possible.add(frozenset({a, b}))

    return possible | set(map(lambda i: frozenset({i}), items))


grid = create_grid()
full_floor = len(grid[0]) - 2  # nr + E
q = []
heapq.heapify(q)
heapq.heappush(q, (
    0,
    1, to_string(grid), possible_items_to_move(grid, 1), [to_string(grid)]))

min_path = []
while q:
    _, floor_nr, grid, items_to_move, prev_grids = heapq.heappop(q)
    grid = parse(grid)
    items_on_4th_floor = items_on_floor(grid, 4)

    if len(items_on_4th_floor) == full_floor:
        print("found", len(prev_grids) - 1)
        for g in min_path:
            print(g)
        break

    next_floors = [next_floor_nr
                   for next_floor_nr in [floor_nr + 1, floor_nr - 1]
                   if 1 <= next_floor_nr <= 4]
    for next_floor in sorted(next_floors, reverse=True):
        for items in items_to_move:
            has_moved, moved_string_grid = move(to_string(grid), items, floor_nr, next_floor)
            if has_moved and moved_string_grid in prev_grids:
                continue

            if has_moved:
                moved_grid = parse(moved_string_grid)
                heapq.heappush(q, (
                    -(100000 * len(items_on_floor(moved_grid, 4)) +
                      100 * len(items_on_floor(moved_grid, 3)) +
                      10 * len(items_on_floor(moved_grid, 2)) +
                      1 * len(items_on_floor(moved_grid, 1))),
                    next_floor,
                    moved_string_grid,
                    possible_items_to_move(moved_grid, next_floor),
                    prev_grids + [moved_string_grid]
                ))
