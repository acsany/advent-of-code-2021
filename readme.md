# 🎄 Advent of Code 2021

Solutions to [Advent of Code 2021](https://adventofcode.com/2021/). Using _Python 3.10_ and _pytest_.

## Puzzle Files

| 🗓 Day | 🧩 Puzzle         | 📄 Script                                   | 🧪 Tests                                              |
| ----: | :---------------- | :------------------------------------------ | :---------------------------------------------------- |
|     1 | Sonar Sweep       | [aoc202101.py](01_sonar_sweep/aoc202101.py) | [test_aoc202101.py](01_sonar_sweep/test_aoc202101.py) |
|     2 | Dive              | [aoc.py](02_dive/aoc.py)                    | [test_aoc.py](02_dive/test_aoc.py)                    |
|     3 | Binary Diagnostic | [aoc.py](02_binary_diagnostic/aoc.py)       | [test_aoc.py](02_binary_diagnostic/test_aoc.py)       |

## Template Usage

To quickly create an entry on a new day, you can run:

```console
$ cp -R 00_template <puzzle_foldername>
```

This command copies the `00_template` folder and pastes it with a new foldername you provide.

## Script And Tests

> The code examples below assume you're in the directory of the specific day.

Copy your _AoC Input_ into `input.txt` and run:

```console
$ python3 aoc.py input.txt
```

The `aoc.py` file will also run even if `input.py` is empty.

To test your solution, copy the _AoC Example Input_ for _Part 1_ `example1.txt`.

Once you have copied the _AoC Example Input_ you must paste the expected parsed into the `test_aoc.py` file, adjust the solution and remove the skip-decorator:

```python
# test_aoc.py

# ...

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

# ...
```

The steps are the same for _Part 2_. However, you must use `example2.txt`, and adjust `test_parse_example2()` and `test_part2_example2()` in `test_aoc.py`.

To run the tests, run:

```console
$ pytest
```

Once you only remove the skip-decorator, the tests will fail by default.
