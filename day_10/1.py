from collections import defaultdict

from models.board import create_int_board, get_coords_around_cross
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()

board = parser.get_board()

for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == '.':
            board.items[i][j] = '-1'

board = create_int_board(board.items)

scores = defaultdict(set)

queue = []

for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == 0:
            queue.append(((i, j), (i, j), 0))

while queue:
    (current_i, current_j), (start_i, start_j), val = queue.pop(0)

    possible_coords = get_coords_around_cross(current_i, current_j, board.height, board.width)
    for (i, j) in possible_coords:
        if board.items[i][j] == 9 and val == 8:
            scores[(start_i, start_j)].add((i, j))
        elif board.items[i][j] == val + 1:
            queue.append(((i, j), (start_i, start_j), val + 1))
print(scores)

sums = 0
for nines in scores:
    sums += len(scores[nines])
print(sums)
