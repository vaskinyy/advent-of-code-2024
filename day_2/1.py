from collections import defaultdict

from models.board import StrBoard, create_str_board, get_coords_around, get_coords_around_cross
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = [[int(i) for i in item.split(' ')] for item in parser.get_input_lines()]

print(lines)

def increasing(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False
        if items[i + 1] - items[i] > 3:
            return False
    return True

def decreasing(items):
    for i in range(len(items) - 1):
        if items[i] <= items[i + 1]:
            return False
        if items[i] - items[i + 1] > 3:
            return False
    return True

safe_levels = [1 if increasing(line) or decreasing(line) else 0 for line in lines]
print(safe_levels)
print(sum(safe_levels))