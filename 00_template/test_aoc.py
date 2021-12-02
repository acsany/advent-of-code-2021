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


@pytest.mark.skip("Not implemented yet.")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert len(example1) > 0
    assert example1 == [
        # TODO: Add expected lines for example1.txt
    ]


@pytest.mark.skip("Not implemented yet.")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    # TODO: Change expected solution for part 1
    assert aoc.part1(example1) == None


@pytest.mark.skip("Not implemented yet.")
def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert len(example2) > 0
    assert example2 == [
        # TODO: Add expected lines for example2.txt
    ]


@pytest.mark.skip("Not implemented yet.")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    # TODO: Change expected solution for part 2
    assert aoc.part2(example2) == None
