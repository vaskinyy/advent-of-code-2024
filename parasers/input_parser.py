import os

from models.board import build_board, StrBoard


class InputParser:
    def __init__(self, test_mode: bool = True):
        self.test_input_lines = None
        self.full_input_lines = None

        self.test_board = None
        self.full_board = None

        self.test_mode = test_mode

    def parse(self):
        if os.path.exists('test_input.txt'):
            with open('test_input.txt', 'r') as f:
                self.test_input_lines = [item.strip() for item in f.readlines() if item.strip()]

        if os.path.exists('full_input.txt'):
            with open('full_input.txt', 'r') as f:
                self.full_input_lines = [item.strip() for item in f.readlines() if item.strip()]

    def build_boards(self):
        if self.test_input_lines:
            self.test_board = build_board(self.test_input_lines)

        if self.full_input_lines:
            self.full_board = build_board(self.full_input_lines)

    def get_input_lines(self):
        return self.test_input_lines if self.test_mode else self.full_input_lines

    def get_board(self) -> StrBoard:
        return self.test_board if self.test_mode else self.full_board

