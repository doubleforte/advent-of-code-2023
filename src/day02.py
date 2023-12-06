# https://adventofcode.com/2023/day/2

from utils.types import DayResult

CUBE_COUNTS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


class Round:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return str((self.red, self.green, self.blue))

    def __repr__(self):
        return str((self.red, self.green, self.blue))

    def is_possible(self):
        return (
            self.red <= CUBE_COUNTS['red']
            and self.green <= CUBE_COUNTS['green']
            and self.blue <= CUBE_COUNTS['blue']
        )

    def max(self, other):
        self.red = max(self.red, other.red)
        self.green = max(self.green, other.green)
        self.blue = max(self.blue, other.blue)


class Game:
    def __init__(self, id: int, rounds: list[Round]):
        self.id = id
        self.rounds = rounds


def parse_round(round) -> Round:
    result = Round(red=0, green=0, blue=0)

    cubes = round.strip().split(',')

    for cube in cubes:
        parts = cube.strip().split(' ')
        color = parts[1]
        count = int(parts[0])
        setattr(result, color, count)
    return result


def parse_game(game: str) -> Game:
    parts = game.split(':')

    id = int(parts[0].split(' ')[1])
    rounds = []

    for round in parts[1].split(';'):
        rounds.append(parse_round(round))

    return Game(id=id, rounds=rounds)


def main(input: str) -> DayResult:
    lines = input.splitlines()

    total1 = 0
    total2 = 0

    for line in lines:
        game = parse_game(line)

        # Part 1
        if all(round.is_possible() for round in game.rounds):
            total1 += game.id

        # Part 2
        maxes = Round(0, 0, 0)
        for round in game.rounds:
            maxes.max(round)
        total2 += maxes.red * maxes.green * maxes.blue

    return total1, total2


# Part 1: 8 / 2176
# Part 2: 2286 / 63700
