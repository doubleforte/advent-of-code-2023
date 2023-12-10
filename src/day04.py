# https://adventofcode.com/2023/day/4

from utils.types import DayResult


def intersection[T](list1: list[T], list2: list[T]) -> list[T]:
    list3 = [value for value in list1 if value in list2]
    return list3


class Card:
    def __init__(self, id: int, numbers: list[int]):
        self.id = id
        self.numbers = numbers

    def __repr__(self):
        return str((self.id, self.numbers))


def convert_to_int_list(str: str) -> list[int]:
    strings = str.strip().split(' ')
    return [int(x.strip()) for x in strings if x != '']


def parse_card(input: str) -> Card:
    parts = input.split(':')
    id = int(parts[0].replace('Card', '').strip())
    numbers = convert_to_int_list(parts[1])
    return Card(id=id, numbers=numbers)


def main(input: str) -> DayResult:
    lines = input.splitlines()

    total1 = 0
    total2 = 0

    for line in lines:
        splits = line.split('|')
        card = parse_card(splits[0])
        my_numbers = convert_to_int_list(splits[1])
        winners = intersection(card.numbers, my_numbers)

        # Part 1
        card_score = 0
        for _ in winners:
            if card_score == 0:
                card_score = 1
            else:
                card_score *= 2

        total1 += card_score

        # Part 2
        # ???

    return total1, total2


# Part 1: 13 / 25004
# Part 2: 0 / 0
