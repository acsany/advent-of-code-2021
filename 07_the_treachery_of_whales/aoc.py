import pathlib
import sys

import statistics
import math

def parse(puzzle_input):
    """Parse input"""
    #return [line for line in puzzle_input.split("\n") if line]
    return [int(d) for d in puzzle_input.strip().split(",") if d]


def cheapest_position(positions):
    return statistics.median(positions)

def fuel_dict(starting_pos, min_pos, max_pos):
    # position, fuel_burned
    fuel_dict = {}
    for target_pos in range(min_pos, max_pos):
        fuel = calculate_fuel(starting_pos, target_pos)
        fuel_dict.setdefault(target_pos, fuel)
    return fuel_dict


def cheapest_position_expensive_rework(positions):
    min_position = min(positions)
    max_position = max(positions)
    fuel_dict_complete = {}
    for pos in positions:
        fd = fuel_dict(pos, min_position, max_position)
        for target_pos, fuel in fd.items():
            fuel_dict_complete.setdefault(target_pos, 0)
            fuel_dict_complete[target_pos] += fuel

    cheapest_pos = None
    min_fuel = 999999999999999999
    for pos, fuel in fuel_dict_complete.items():
        #print(pos, fuel)
        if fuel < min_fuel:
            min_fuel = fuel
            cheapest_pos = pos

    return cheapest_pos, min_fuel

def cheapest_position_expensive(positions):
    # min_position = min(positions)
    # max_position = max(positions)
    # fuel_dict = {}
    # for pos in positions:
    #     for target_pos in range(min_position, max_position):
    #         fuel = abs(pos-target_position)
    #         fuel_dict.setdefault(target_pos, fu)
    #         print(fuel_dict)

    return math.ceil(sum(positions)/len(positions))


def calculate_fuel(pos, target):
    cost = 0
    sum_cost = 0
    for i in range(abs(pos-target)):
        cost += 1
        sum_cost += cost
        #print(i, cost, sum_cost)
    
    return sum_cost

def part1(starting_positions):
    """Solve part 1"""
    solution = 0
    target_position = cheapest_position(starting_positions)
    for pos in starting_positions:
        solution += abs(pos-target_position)

    return solution



def part2(starting_positions):
    """Solve part 2"""
    _, solution = cheapest_position_expensive_rework(starting_positions)

    return solution


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
