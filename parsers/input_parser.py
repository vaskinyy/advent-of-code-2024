import os

from models.board import build_board, StrBoard


class InputParser:
    def __init__(self, test_mode: bool = True, strip=True):
        self.test_input_lines = None
        self.full_input_lines = None

        self.test_board = None
        self.full_board = None

        self.test_mode = test_mode
        self.strip = strip

    def parse(self):
        if os.path.exists('test_input.txt'):
            with open('test_input.txt', 'r') as f:

                if self.strip:
                    self.test_input_lines = [item.strip() for item in f.readlines() if item.strip()]
                else:
                    self.test_input_lines = [item.strip() for item in f.readlines()]

        if os.path.exists('full_input.txt'):
            with open('full_input.txt', 'r') as f:
                if self.strip:
                    self.full_input_lines = [item.strip() for item in f.readlines() if item.strip()]
                else:
                    self.full_input_lines = [item.strip() for item in f.readlines()]

    def build_boards(self):
        if self.test_input_lines:
            self.test_board = build_board(self.test_input_lines)

        if self.full_input_lines:
            self.full_board = build_board(self.full_input_lines)

    def get_input_lines(self):
        return self.test_input_lines if self.test_mode else self.full_input_lines

    def get_board(self) -> StrBoard:
        return self.test_board if self.test_mode else self.full_board

    def get_board_set(self):
        board_set = set()
        board = self.get_board()
        for i in range(board.height):
            for j in range(board.width):
                board_set.add((i, j))
        return board_set
