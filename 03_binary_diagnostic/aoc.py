import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n") if line]

def create_empty_string_list(length):
    return ["" for _ in range(length)]

def cut_list(lines):
    """Nicer solution"""
    input_len = len(lines[0])
    cut = create_empty_string_list(input_len)

    for l in lines:
        for i, digit in enumerate(l):
            cut[i] += digit

    return cut


def dec(bit_string):
    return int(bit_string, 2)


def part1(lines):
    """Solve part 1"""
    gamma_rate = ""
    epsilon_rate = ""
    
    for digit_line in cut_list(lines):
        ones = digit_line.count("1")
        zeros = digit_line.count("0")

        gamma_rate += "1" if ones > zeros else "0"
        epsilon_rate += "0" if ones > zeros else "1"
    
    return dec(gamma_rate) * dec(epsilon_rate)


def check_lines(idx, lines, default_return):
    ones = cut_list(lines)[idx].count("1")
    zeros = cut_list(lines)[idx].count("0")
    other_digit = "0" if default_return == "1" else "1"

    if zeros > ones:
        return other_digit
    else:
        return default_return



def get_rate(num, lines):
    max_length = len(lines[0])
    remaining_lines = lines

    for i in range(max_length):
        oxy_remaining = []
        look_for_number = check_lines(i, remaining_lines, default_return=num)
        for l in remaining_lines:
            digit = l[i]
            if digit == look_for_number:
                oxy_remaining.append(l)
        if len(oxy_remaining) == 1:
            return oxy_remaining[0]

        remaining_lines = oxy_remaining


def part2(lines):
    """Solve part 2"""
    oxygen_rate = get_rate("1", lines)
    co2_rate = get_rate("0", lines)
    
    return dec(oxygen_rate) * dec(co2_rate)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
