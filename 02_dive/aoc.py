import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""

    return [line for line in puzzle_input.split("\n") if line]


def part1(lines):
    """Solve part 1"""
    horizontal_pos = 0
    depth_pos = 0
    for l in lines:
        match l.split():
            case ["forward", val]:
                horizontal_pos += int(val)
            case ["down", val]:
                depth_pos += int(val)
            case ["up", val]:
                depth_pos -= int(val)

    return horizontal_pos * depth_pos


def part2(lines):
    """Solve part 2"""
    horizontal_pos = 0
    depth_pos = 0
    aim = 0

    for l in lines:
        match l.split():
            case ["forward", val]:
                horizontal_pos += int(val)
                depth_pos += aim * int(val)
            case ["down", val]:
                aim += int(val)
            case ["up", val]:
                aim -= int(val)

    return horizontal_pos * depth_pos


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
