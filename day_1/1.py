from collections import defaultdict

from models.board import StrBoard, create_str_board, get_coords_around, get_coords_around_cross
from parsers.input_parser import InputParser

test_mode = True

parser = InputParser(test_mode)
parser.parse()

pairs = [[int(i) for i in item.split('   ')] for item in parser.get_input_lines()]

first_list = [item[0] for item in pairs]
second_list = [item[1] for item in pairs]

print(first_list)
print(second_list)

sorted_first_list = sorted(first_list)
sorted_second_list = sorted(second_list)


print(sorted_first_list)
print(sorted_second_list)

distances = [abs(pair[0] - pair[1]) for pair in zip(sorted_first_list, sorted_second_list)]
print(distances)
print(sum(distances))