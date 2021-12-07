import pathlib
import sys

from itertools import zip_longest

# test

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n") if line]

def convert_to_coordinates(lines):
    coords = []
    for l in lines:
        clean_line = l.replace(" -> ", ",")
        coords.append([int(d) for d in clean_line.split(",")])
    return coords


def get_line_coords(line_in):
    line_coords = []
    x1, y1, x2, y2 = line_in

    if x1 <= x2:
        x2 += 1
        x_step = 1
    else:
        x2 -= 1
        x_step = -1
    
    if y1 <= y2:
        y2 += 1
        y_step = 1
    else:
        y2 -= 1
        y_step = -1

    x_range = list(range(x1, x2, x_step))
    y_range = list(range(y1, y2, y_step))
    shorter_list = x_range if len(x_range) < len(y_range) else y_range

    line_coords = zip_longest(x_range, y_range, fillvalue=shorter_list[0])
    return list(line_coords)

def get_max_coords(lines):
    max_x = 0
    max_y = 0
    for l in lines:
        x1, y1, x2, y2 = l
        this_max_x = max(x1, x2)
        this_max_y = max(y1, y2)
        max_x = this_max_x if this_max_x > max_x else max_x
        max_y = this_max_y if this_max_y > max_y else max_y
    return (max_x, max_y)

def get_field(max_x, max_y):
    field = []
    x_line = [0 for x in range(max_x+1)]
    for y in range(max_y+1):
        field.append(x_line)
    
    return field

def draw_line_in_field(field, line, draw_diagonal=False):

    is_45 = is_45_deg(line)
    is_horizontal = not is_45

    draw = False
    if is_horizontal:
        draw = True
    else:
        if is_45 and draw_diagonal:
            draw = True

    if draw:
        line_coords = get_line_coords(line)

        # for y_idx, line in enumerate(field):
        #     print(y_idx, line)
        for coord_tuple in line_coords:
            x, y = coord_tuple
            #if y_idx == y and field[y_idx][x] == 0:
            l = field[y][:]
            l[x] += 1
            field[y] = l[:]
        # for x, y in line_coords:
        #     line = field[y][:]
        #     print(x, y)
        #     print(line)
        #     print(line)
        #     # tthe error is somewhere here
        #     line[x] += 1
        #     field[y] = line
    return field

def draw_all_lines_in_field(field_in, lines, draw_diagonal=False):
    field = field_in
    for l in lines:
        field = draw_line_in_field(field, l, draw_diagonal)
    
    return field

def get_intersections(field):
    intersections = 0
    for l in field:
        for count in l:
            if count > 1:
                intersections += 1
    return intersections


def is_45_deg(line):
    coords = get_line_coords(line)
    test_sum = sum(coords[0])
    if coords[0][0] - coords[0][1] == coords[-1][0] - coords[-1][1]:
        return True
    
    for val in coords:
        if sum(val) != test_sum:
            return False
    else:
        return True

    # is_45 = True if sum
    # #is_45 = coords[0][0] - coords[0][1] == coords[-1][0] - coords[-1][1]
    # print(is_45)
    # return is_45

def part1(lines):
    """Solve part 1"""
    coordinates = convert_to_coordinates(lines)
    max_x, max_y = get_max_coords(coordinates)
    field = get_field(max_x, max_y)
    field_drawn = draw_all_lines_in_field(field, coordinates)
    intersections = get_intersections(field_drawn)

    return intersections


def part2(lines):
    """Solve part 2"""
    coordinates = convert_to_coordinates(lines)
    max_x, max_y = get_max_coords(coordinates)
    field = get_field(max_x, max_y)
    field_drawn = draw_all_lines_in_field(field, coordinates, draw_diagonal=True)
    intersections = get_intersections(field_drawn)

    return intersections


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
