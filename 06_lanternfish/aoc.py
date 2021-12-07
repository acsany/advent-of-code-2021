import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n") if line]

def parse_line(line):
    return [int(f) for f in line.split(",")]

def get_data(lines):
    data_in = lines[0]
    return parse_line(data_in)

def fish_count(day, state_by_day):
    return len(state_by_day[day-1])

def fish_count_optimized(state_by_day):
    d = list(state_by_day)
    return len(d[0])

def fish_count_dict(fish_dict):
    return sum(fish_dict.values())

def get_inital_fish_dict(lines):
    line = parse_line(lines[0])
    d = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    for age in line:
        d[age] += 1
    
    return d

def update_fish_dict(dict_in):
    dict_out = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    for k, count in dict_in.items():
        if k == 0:
            dict_out[8] += count
            dict_out[6] += count
        else:
            dict_out[k-1] += count
    
    return dict_out

def extrapolate_line(line_in):
    line_out = []
    new_spawns = []
    for d in line_in:
        new_d = d-1
        if new_d < 0:
            new_d = 6
            new_spawns.append(8)
        
        line_out.append(new_d)
    
    return line_out + new_spawns

def extrapolate_data(inital_data, until_day):
    data = []
    day_data = inital_data
    for day in range(until_day):
        next_day_data = extrapolate_line(day_data)
        data.append(next_day_data)
        day_data = next_day_data
    
    return data


def get_day_data(initial_dict, until_day):
    day_data = initial_dict
    for day in range(until_day):
        day_data = update_fish_dict(day_data)
    
    return day_data

def part1(lines):
    """Solve part 1"""
    days = 80
    dict_in = get_inital_fish_dict(lines)
    data = get_day_data(dict_in, days)
    count = fish_count_dict(data)

    return count



def part2(lines):
    """Solve part 2"""
    days = 256
    dict_in = get_inital_fish_dict(lines)
    data = get_day_data(dict_in, days)
    count = fish_count_dict(data)

    return count


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
