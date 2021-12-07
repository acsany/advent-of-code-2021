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


# def test_parse_example1(example1):
#     """Test that input is parsed properly"""
#     assert len(example1) > 0
#     assert example1 == [
#         # TODO: Add expected lines for example1.txt
#     ]

def test_numbers_drawn(example1):
    assert aoc.get_numbers_drawn(example1) == [
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    ]

def test_get_boards(example1):
    boards = [
        [
            [22, 13, 17, 11,  0,],
            [8,  2, 23,  4, 24,],
            [21,  9, 14, 16,  7,],
            [6, 10,  3, 18,  5,],
            [1, 12, 20, 15, 19,],
        ],
        [
            [3, 15,  0,  2, 22,],
            [9, 18, 13, 17,  5,],
            [19,  8,  7, 25, 23,],
            [20, 11, 10, 24,  4,],
            [14, 21, 16, 12,  6,],
        ],
        [
            [14, 21, 17, 24,  4,],
            [10, 16, 15,  9, 19,],
            [18,  8, 23, 26, 20,],
            [22, 11, 13,  6,  5,],
            [2,  0, 12,  3,  7,],
        ]
    ]

    assert aoc.get_boards(example1) == boards

def test_check_winning_board():
    board_data = [
            [22, 13, 17, 11,  0,],
            [8,  2, 23,  4, 24,],
            [21,  9, 14, 16,  7,],
            [6, 10,  3, 18,  5,],
            [1, 12, 20, 15, 19,],
        ]
    
    # Winning row
    this_draw = [22, 13, 17, 11,  0,]
    b = aoc.Board(board_data, this_draw)
    assert b.has_win() == True
    assert b.winning_numbers_data == {
            "rows": {
                0: [22, 13, 17, 11,  0,],
                1: [],
                2: [],
                3: [],
                4: [],
            },
            "columns": {
                0: [22,],
                1: [13,],
                2: [17,],
                3: [11,],
                4: [0,],
            }
        }

    this_draw = [8,  2, 23,  4, 24,]
    b_1 = aoc.Board(board_data, this_draw)
    assert b_1.has_win() == True

    # Winning column 1
    this_draw = [22,  8, 21,  6, 1,]
    b_2 = aoc.Board(board_data, this_draw)
    assert b_2.has_win() == True

    # Winning column 2
    this_draw = [13,  2, 9,  10, 12,]
    b_3 = aoc.Board(board_data, this_draw)
    assert b_3.has_win() == True


def test_board_all_numbers():
    board_data = [
            [22, 11, 13,  6,  5,],
            [2,  0, 12,  3,  7,],
        ]

    draw = []
    b = aoc.Board(board_data, draw)
    assert b.all_numbers == [22, 11, 13,  6,  5, 2,  0, 12,  3,  7,]

def test_winning_board_unmarked_sum():
    board_data = [
            [14, 21, 17, 24,  4,],
            [10, 16, 15,  9, 19,],
            [18,  8, 23, 26, 20,],
            [22, 11, 13,  6,  5,],
            [2,  0, 12,  3,  7,],
        ]

    draw = [
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    ]
    b = aoc.Board(board_data, draw)
    assert b.has_win() == True
    assert b.get_unmarked_numbers() == [
        10, 16, 15,     19,
        18,  8,     26, 20,
        22,     13,  6,
                12,  3,
    ]
    assert b.get_unmarked_sum() == 188
    assert b.last_draw == 24
    assert b.get_board_solution() == 4512


def test_part1_example1(example1):
    """Test part 1 on example input"""
    # TODO: Change expected solution for part 1
    assert aoc.part1(example1) == 4512


@pytest.mark.skip("Not implemented yet.")
def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert len(example2) > 0
    assert example2 == [
        # TODO: Add expected lines for example2.txt
    ]


def test_part2_example2(example2):
    """Test part 2 on example input"""
    # TODO: Change expected solution for part 2
    assert aoc.part2(example2) == 1924
