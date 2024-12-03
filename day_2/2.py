import copy
from collections import defaultdict

from models.board import StrBoard, create_str_board, get_coords_around, get_coords_around_cross
from parasers.input_parser import InputParser

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

counter = 0
for line in lines:
    new_lines = []
    for i in range(len(line)):
        new_line = copy.deepcopy(line)
        new_line.pop(i)
        new_lines.append(new_line)
    new_lines.append(line)

    for check_line in new_lines:
        if increasing(check_line) or decreasing(check_line):
            counter += 1
            break
print(counter)