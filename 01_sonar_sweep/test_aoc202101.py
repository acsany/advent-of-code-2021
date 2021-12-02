import pathlib
import pytest
import aoc202101 as aoc

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
    assert example1 == [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]


def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]


def test_parse_example2(example2):
    """Test that input is parsed properly"""

    assert aoc.parse_into_summed_list(example2) == [
        607,
        618,
        618,
        617,
        647,
        716,
        769,
        792,
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 7


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 5
