# Stolen (and adapted) from https://github.com/Anshuman-UCSB/Advent-Of-Code/blob/master/2023/Python/main.py
# https://www.youtube.com/watch?v=X1Q-YI3knL4

import fnmatch
import os
import traceback
import importlib
import argparse
import time

TITLE = 'ADVENT OF CODE 2023'


def get_days_range() -> range:
    """
    Get the count of the number of days based on the number `src/day0x.py` files.
    """

    dir_path = r'src'
    total_days = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
    # `range` does not include the `stop` arg, so we need to go one beyond.
    return range(1, total_days + 1)


days = [None] + [importlib.import_module(f'src.day{i:02d}') for i in get_days_range()]

parser = argparse.ArgumentParser()
parser.add_argument('day', nargs='?', type=int, help='Select just one day to run')
parser.add_argument(
    '-e', '--example', action='store_true', help='Run examples instead of real input'
)
parser.add_argument(
    '-d', '--debug', action='store_true', help='Include error outputs for example cases'
)

args = parser.parse_args()
if args.debug:
    args.example = True


def runDay(day, path=None):
    path = path or f'data/day{day:02d}/input.txt'
    with open(path, 'r') as f:
        inp = f.read().strip()
        start_time = time.time()

        try:
            results = days[day].main(inp)
        except Exception as e:
            if args.debug:
                traceback.print_exc()
            results = (str(e), None)

        elapsed = time.time() - start_time
        return results, elapsed * 1000


def printDay(intro, results, elapsed) -> None:
    print(intro)

    if results is None:
        print('  No output')
    else:
        print('  Part 1:', results[0])

        if results[1] is not None:
            print('  Part 2:', results[1])

        print(f'  took {int(elapsed)}ms')


def runExamples(day) -> None:
    example_paths = sorted(os.listdir(f'data/day{day:02d}/example-input'))

    for example_path in example_paths:
        print('=====')

        printDay(
            f'Example {example_path}:',
            *runDay(day, f'data/day{day:02d}/example-input/' + example_path),
        )
        print()


if args.day is None:
    print(f' --- {TITLE} ---')

    if args.example:
        print('(example flag ignored due to running all days)')

    print()
    total = 0

    for i in get_days_range():
        results, elapsed = runDay(i)

        if results is None:
            break

        printDay(f'Day {i}:', results, elapsed)
        total += elapsed

    print(f'\nAll days combined took {int(total)}ms')
else:
    if args.example:
        runExamples(args.day)
    else:
        printDay(f'Day {args.day}:', *runDay(args.day))
