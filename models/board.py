import copy
from typing import List

from attrs import define


@define
class StrBoard:
    items: List[List[str]]
    width: int
    height: int

    def __repr__(self):
        output = []
        for line in self.items:
            for item in line:
                output.append(str(item))
            output.append("\n")
        return ''.join(output)


@define
class IntBoard:
    items: List[List[int]]
    width: int
    height: int

    def __repr__(self):
        output = []
        for line in self.items:
            for item in line:
                output.append(str(item))
            output.append("\n")
        return ''.join(output)


def create_str_board(items: List[List[str]]) -> StrBoard:
    return StrBoard(copy.deepcopy(items), len(items[0]), len(items))


def create_int_board(items: List[List[str]]) -> IntBoard:
    new_items = copy.deepcopy(items)
    for i in range(len(new_items)):
        for j in range(len(new_items[i])):
            new_items[i][j] = int(new_items[i][j])
    return IntBoard(new_items, len(items[0]), len(items))


def build_board(input_data):
    board = []
    for line in input_data:
        board_line = []
        for item in line:
            board_line.append(item)
        board.append(board_line)

    return create_str_board(board)


def get_coords_around(i, j, height, width):
    coordinates = []
    if i > 0 and j > 0:
        coordinates.append((i - 1, j - 1))
    if i > 0:
        coordinates.append((i - 1, j))
    if i > 0 and j < (width - 1):
        coordinates.append((i - 1, j + 1))
    if j > 0:
        coordinates.append((i, j - 1))
    if j < (width - 1):
        coordinates.append((i, j + 1))
    if i < (height - 1) and j > 0:
        coordinates.append((i + 1, j - 1))
    if i < (height - 1):
        coordinates.append((i + 1, j))
    if i < (height - 1) and j < (width - 1):
        coordinates.append((i + 1, j + 1))
    return coordinates


def get_coords_around_cross(i, j, height, width):
    coordinates = []
    if i > 0:
        coordinates.append((i - 1, j))
    if j > 0:
        coordinates.append((i, j - 1))
    if j < (width - 1):
        coordinates.append((i, j + 1))
    if i < (height - 1):
        coordinates.append((i + 1, j))
    return coordinates


def transpose(items):
    return list(zip(*items))


def get_transposed_board(board: StrBoard) -> StrBoard:
    items = transpose(board.items)
    return StrBoard(items, len(items[0]), len(items))


def get_rotated_90(board: StrBoard) -> StrBoard:
    items = transpose(board.items)[::-1]
    return StrBoard(items, len(items[0]), len(items))


def rotate_90_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
