# https://adventofcode.com/2023/day/1

from utils.types import DayResult


NUMBERS_AS_WORDS = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]


def main(input: str) -> DayResult:
    lines = input.splitlines()

    total1 = 0
    total2 = 0

    for line in lines:
        # Part 1
        digits = [int(x) for x in line if x.isdigit()]
        if digits:
            total1 += int(f'{digits[0]}{digits[-1]}')

        # Part 2
        digits = [int(x) for x in translate(line) if x.isdigit()]
        if digits:
            total2 += int(f'{digits[0]}{digits[-1]}')

    return total1, total2


def translate(line: str) -> str:
    for num, name in enumerate(NUMBERS_AS_WORDS):
        # Pad the number with its name so we don't break overlaps.
        line = line.replace(name, f'{name}{num}{name}')
    return line


# Part 1: 142 / 55971
# Part 2: 281 / 54719
