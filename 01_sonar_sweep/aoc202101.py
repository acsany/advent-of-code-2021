import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def parse_into_summed_list(numbers):
    """Parse measurement groups"""
    summed_list = []
    for i, num in enumerate(numbers):
        try:
            this_sum = num + numbers[i+1] + numbers[i+2]
            summed_list.append(this_sum)
        except IndexError:
            pass
    return summed_list


def part1(numbers):
    """Solve part 1"""
    numbers_increased = 0
    for i, num in enumerate(numbers, start=0):
        num_before = numbers[i-1]
        if i != 0 and num > num_before:
            numbers_increased += 1
    
    return numbers_increased


def part2(numbers):
    """Solve part 2"""
    summed_numbers = parse_into_summed_list(numbers)
    return part1(summed_numbers)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)
        print(part2(numbers))
