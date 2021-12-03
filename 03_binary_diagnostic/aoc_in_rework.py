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

def check_lines_new(idx, lines, default_return="1"): 
    ones = 0
    zeros = 0
    for l in lines:
        digit = l[idx]
        if digit == "1":
            ones += 1
        else:
            zeros += 1
    
    if default_return == "1":
        if ones > zeros:
            return "1"
        
        elif zeros > ones:
            return "0"
        
        else:
            return default_return
    
    if default_return == "0":
        if ones < zeros:
            return "1"
        
        elif zeros < ones:
            return "0"
        
        else:
            return default_return

def check_lines(idx, digit_line, default_return="1"): 
    ones = 0
    zeros = 0
    for digit in digit_line:
        if digit == "1":
            ones += 1
        else:
            zeros += 1

    if default_return == "1":
        if ones > zeros:
            return "1"
        
        elif zeros > ones:
            return "0"
        
        else:
            return default_return
    
    if default_return == "0":
        if ones < zeros:
            return "1"
        
        elif zeros < ones:
            return "0"
        
        else:
            return default_return


def get_rate_old(num, lines):
    max_length = len(lines[0])
    remaining_lines = lines

    for i in range(max_length):
        oxy_remaining = []
        look_for_number = check_lines_new(i, remaining_lines, default_return=num)
        for l in remaining_lines:
            digit = l[i]
            if digit == look_for_number:
                oxy_remaining.append(l)
        if len(oxy_remaining) == 1:
            print(dec(oxy_remaining[0]))
            return oxy_remaining[0]

        remaining_lines = oxy_remaining

def get_rate(num, lines):
    remaining_lines = lines

    for i, digit_line in enumerate(cut_list(lines)):
        oxy_remaining = []
        look_for_number = check_lines(i, digit_line, default_return=num)
        print("---")
        print(look_for_number)
        look_for_number = check_lines_new(i, remaining_lines, default_return=num)
        print(look_for_number)
        print("---")
        
        for l in remaining_lines:
            digit = l[i]
            if digit == look_for_number:
                oxy_remaining.append(l)
        if len(oxy_remaining) == 1:
            print(dec(oxy_remaining[0]))
            return oxy_remaining[0]

        remaining_lines = oxy_remaining


def part2(lines):
    """Solve part 2"""
    oxygen_rate = get_rate("1", lines)
    co2_rate = get_rate("0", lines)
    
    return dec(oxygen_rate) * dec(co2_rate)

def part2_old(lines):
    """Solve part 2"""
    oxygen_rate = get_rate("1", lines)
    co2_rate = get_rate("0", lines)
    
    return dec(oxygen_rate) * dec(co2_rate)

def part2_deadend(lines):
    """Solve part 2"""
    digit_line = cut_list(lines)[0]
    ones = digit_line.count("1")
    zeros = digit_line.count("0")
    print(digit_line)
    print(ones, zeros)
    most_num = "1" if ones > zeros else "0"
    least_num = "0" if ones > zeros else "1"
    print(most_num, least_num)
    
    last_idx_most_num = digit_line.rfind(most_num)-1
    oxygen_rate = lines[last_idx_most_num]
    print(last_idx_most_num, oxygen_rate)
    
    last_idx_least_num = digit_line.rfind(least_num)
    co2_rate = lines[last_idx_least_num]
    
    return dec(oxygen_rate) * dec(co2_rate)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
