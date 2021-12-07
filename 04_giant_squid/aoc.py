import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n") if line]


def get_numbers_drawn(lines):
    return [int(l) for l in lines[0].split(",")]

def get_boards(lines):
    boards_all = lines[1:]
    board_line_count = 5
    boards = []
    current_board = []
    for i, line in enumerate(boards_all):
        if i % board_line_count == 0 and i != 0:
            print(current_board)
            boards.append(current_board)
            current_board = []
        parsed_line = [int(l) for l in line.strip().split()]
        current_board.append(parsed_line)
    boards.append(current_board)
    
    return boards

class Board():

    def __init__(self, board_lines, numbers_drawn):
        print("...created Board")
        self.lines = board_lines
        self.all_numbers = self.get_all_number()
        self.numbers_drawn = numbers_drawn
        self.no_win_numbers = []
        self.winning_round = None
        self.winning_numbers = []
        self.winning_numbers_data = {
            "rows": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
            },
            "columns": {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
            }
        }
        self.last_draw = None
    
    def check_win(self):
        
        all_numbers = []
        for round, n in enumerate(self.numbers_drawn):
            for v_i, l in enumerate(self.lines):
                for h_i, board_number in enumerate(l):
                    if n == board_number:
                        win_data = (v_i, h_i, board_number)
                        self.winning_numbers_data["rows"][v_i].append(board_number)
                        self.winning_numbers_data["columns"][h_i].append(board_number)
                        self.winning_numbers.append(board_number)
                    for area in self.winning_numbers_data.values():
                        for data in area.values():
                            if len(data) == 5:
                                self.last_draw = n
                                self.winning_round = round
                                return True


    def has_win(self):
        return self.check_win()
    
    def get_unmarked_numbers(self):
        unmarked_numbers = []
        print(self.winning_numbers_data)
        for n in self.all_numbers:
            if n not in self.winning_numbers:
                unmarked_numbers.append(n)
        
        return unmarked_numbers
    
    def get_all_number(self):
        all_numbers = []
        for l in self.lines:
            for n in l:
                all_numbers.append(n)
        
        return all_numbers
    
    def get_unmarked_sum(self):
        return sum(self.get_unmarked_numbers())
    
    def get_board_solution(self):
        print("Last drawed number", self.last_draw)
        return self.get_unmarked_sum() * self.last_draw


def part1(lines):
    """Solve part 1"""
    numbers_drawn = get_numbers_drawn(lines)
    boards_data = get_boards(lines)
    boards_classes = []
    winning_round = len(numbers_drawn) + 1
    winning_board = None
    for i, board_data in enumerate(boards_data):
        b = Board(board_data, numbers_drawn)
        if b.has_win() == True:
            print("BOARD:", i)
            print("ROUND:", b.winning_round )
            print(b.winning_round < winning_round)
            if b.winning_round < winning_round:
                winning_round = b.winning_round
                winning_board = b
    
    return winning_board.get_board_solution()



def part2(lines):
    """Solve part 2"""
    numbers_drawn = get_numbers_drawn(lines)
    boards_data = get_boards(lines)
    boards_classes = []
    winning_round = 0
    winning_board = None
    for i, board_data in enumerate(boards_data):
        b = Board(board_data, numbers_drawn)
        if b.has_win() == True:
            print("BOARD:", i)
            print("ROUND:", b.winning_round )
            print(b.winning_round < winning_round)
            if b.winning_round > winning_round:
                winning_round = b.winning_round
                winning_board = b
    
    return winning_board.get_board_solution()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(f"PART 1: {part1(lines)}")
        print(f"PART 2: {part2(lines)}")
