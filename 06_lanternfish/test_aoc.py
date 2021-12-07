import pathlib
import pytest
import aoc as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert len(example1) > 0
    assert example1 == [
        "3,4,3,1,2",
    ]


def test_parse_line():
    l = "3,4,3,1,2"
    assert aoc.parse_line(l) == [3,4,3,1,2]


def test_parse_get_data(example1):
    initial_state = aoc.get_data(example1)
    # check_day = 18
    # expected_val = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
    assert initial_state == [3,4,3,1,2]

def test_parse_get_inital_fish_dict(example1):
    initial_state = aoc.get_inital_fish_dict(example1)
    # check_day = 18
    # expected_val = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
    assert initial_state == {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 1,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

def test_update_dict_simple(example1):
    dict_in = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 1,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    expected_dict = {
        0: 1,
        1: 1,
        2: 2,
        3: 1,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    assert aoc.update_fish_dict(dict_in) == expected_dict

def test_extrapolate_line_simple():
    line_in = [3,4,3,1,2]
    line_out = [2,3,2,0,1]

    assert aoc.extrapolate_line(line_in) == line_out

def test_input_to_dict():
    line_in = ["0,1,0,5,6,0,1,2,2,3,7,8"]
    dict_in = aoc.get_inital_fish_dict(line_in)
    assert dict_in[0] == 3

def test_update_dict_complex(example1):
    line_in = ["0,1,0,5,6,0,1,2,2,3,7,8"]
    line_out = [6,0,6,4,5,6,0,1,1,2,6,7,8,8,8]
    dict_in = aoc.get_inital_fish_dict(line_in)
    dict_out = aoc.update_fish_dict(dict_in)

    assert dict_out[0] == 2
    assert dict_out[6] == 4
    assert dict_out[7] == 1
    assert dict_out[8] == 3


def test_extrapolate_line_complex():
    line_in = [0,1,0,5,6,0,1,2,2,3,7,8]
    line_out = [6,0,6,4,5,6,0,1,1,2,6,7,8,8,8]
    
    assert aoc.extrapolate_line(line_in) == line_out


def test_data_day_1(example1):
    day = 1
    expected_val =[[2,3,2,0,1]]
    initial_state = aoc.get_data(example1)
    data = aoc.extrapolate_data(initial_state, day)
    assert len(data) == day
    assert data == expected_val

@pytest.mark.skip("Not implemented yet.")
def test_data_day_1_optimized(example1):
    day = 1
    expected_val =[[2,3,2,0,1]]
    initial_state = aoc.get_data(example1)
    data = aoc.get_day_data(initial_state, day)
    d = list(data)
    #print(list(data))
    assert len(d) == day
    assert d == expected_val


def test_data_day_18(example1):
    day = 18
    expected_val = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
    initial_state = aoc.get_data(example1)
    data = aoc.extrapolate_data(initial_state, day)
    assert len(data) == day
    assert data[-1] == expected_val


def test_data_day_18_optimized(example1):
    day = 18
    #expected_val =[[6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]]
    dict_in = aoc.get_inital_fish_dict(example1)
    assert isinstance(dict_in, dict)
    data = aoc.get_day_data(dict_in, day)
    assert isinstance(data, dict)

def test_fish_count(example1):
    day = 18
    dict_in = aoc.get_inital_fish_dict(example1)
    data = aoc.get_day_data(dict_in, day)

    assert aoc.fish_count_dict(data) == 26


def test_part1_example1(example1):
    """Test part 1 on example input"""
    # TODO: Change expected solution for part 1
    assert aoc.part1(example1) == 5934

# test after 80 days

@pytest.mark.skip("Not implemented yet.")
def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert len(example2) > 0
    assert example2 == [
        # TODO: Add expected lines for example2.txt
    ]


def test_part2_example1(example1):
    """Test part 2 on example input"""
    # TODO: Change expected solution for part 2
    assert aoc.part2(example1) == 26984457539
