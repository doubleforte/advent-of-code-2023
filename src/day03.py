# https://adventofcode.com/2023/day/3

from typing import Tuple
from utils.types import DayResult

Point = complex
Grid = dict[Point, str]

ADJACENT_POINTS = [
    Point(-1, 1),  # Top left
    Point(0, 1),  # Top middle
    Point(1, 1),  # Top right
    Point(-1, 0),  # Middle left
    # Point(0, 0),  # Itself
    Point(1, 0),  # Middle Right
    Point(-1, -1),  # Bottom left
    Point(0, -1),  # Bottom middle
    Point(1, -1),  # Bottom right
]


def get_adjacent_parts(grid: Grid, position: Point) -> set[Point]:
    parts = set()

    for direction in ADJACENT_POINTS:
        parts.add(get_part_number(grid, position + direction))

    # Remove `None` from the result set.
    return parts - {None}


def get_part_number(grid: Grid, position: Point) -> Tuple[Point, int] | None:
    if position not in grid or not grid[position].isnumeric():
        return None

    # Set cursor to the beginning of the number.
    while position - 1 in grid and grid[position - 1].isnumeric():
        position -= 1

    # Get the number.
    start = position
    number = ''
    while position in grid and grid[position].isnumeric():
        number += grid[position]
        position += 1

    # Use `start` so the combination is unique.
    return start, int(number)


def main(input: str) -> DayResult:
    grid: Grid = {}
    symbols = []

    lines = input.splitlines()

    total1 = 0
    total2 = 0

    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            if value != '.':
                grid[Point(x, y)] = value

                if not value.isnumeric():
                    symbols.append(Point(x, y))

    # Part 1
    parts = set()
    for symbol in symbols:
        parts |= get_adjacent_parts(grid, symbol)
    for part in parts:
        total1 += part[1]

    # Part 2
    for symbol in symbols:
        if grid[symbol] != '*':
            continue

        parts = list(get_adjacent_parts(grid, symbol))
        if len(parts) == 2:
            total2 += parts[0][1] * parts[1][1]  # type: ignore

    return total1, total2


# Part 1: 4361 / 538046
# Part 2: 467835 / 81709807
