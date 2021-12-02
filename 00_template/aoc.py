import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n") if line]


def part1(lines):
    """Solve part 1"""
    solution = 0
    for l in lines:
        solution += int(l)

    return solution


def part2(lines):
    """Solve part 2"""
    solution = 0
    for l in lines:
        solution += int(l)

    return solution


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
