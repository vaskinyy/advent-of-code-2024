from collections import defaultdict
from itertools import combinations

from parsers.input_parser import InputParser

test_mode = True

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()

board = parser.get_board()
board_set = parser.get_board_set()
antennas = defaultdict(list)

for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] != '.' and board.items[i][j] != '#':
            antennas[board.items[i][j]].append((i, j))

print(antennas)

antinodes = set()

for name in antennas:
    items = antennas[name]
    unique_pairs = combinations(items, 2)
    for coord1, coord2 in unique_pairs:
        left_distance = (coord1[0] - coord2[0], coord1[1] - coord2[1])
        left_coord = (coord2[0] - left_distance[0], coord2[1] - left_distance[1])
        if left_coord in board_set:
            antinodes.add(left_coord)

        right_distance = (coord2[0] - coord1[0], coord2[1] - coord1[1])
        right_coord = (coord1[0] - right_distance[0], coord1[1] - right_distance[1])
        if right_coord in board_set:
            antinodes.add(right_coord)
print(len(antinodes))

