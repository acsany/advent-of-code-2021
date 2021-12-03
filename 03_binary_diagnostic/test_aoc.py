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
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 198


def test_cut_list(example1):
    """Test part 1 on example input"""
    example = [
        "abc",
        "def",
    ]
    cut = [
        "ad",
        "be",
        "cf",
    ]
    assert aoc.cut_list(example) == cut

def test_dec():
    assert aoc.dec("10110") == 22

def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert len(example2) > 0
    assert example2 == [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 230

