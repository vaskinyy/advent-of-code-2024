
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()

board = parser.get_board()

board_items = set()
for i in range(board.height):
    for j in range(board.width):
        board_items.add((i, j))
print(board_items)

x_locations = []
for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == 'X':
            x_locations.append((i, j))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

counter = 0

for x_location in x_locations:
    for direction in directions:
        current_location = x_location
        for letter in ['M', 'A', 'S']:
            next_location = (current_location[0] + direction[0], current_location[1] + direction[1])
            if next_location in board_items and board.items[next_location[0]][next_location[1]] == letter:
                if letter == 'S':
                    counter += 1
                    break
                current_location = next_location
            else:
                break
print(counter)
