from models.board import build_board
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode, strip=False)
parser.parse()

board_items = []
movements = []
parse_board = True
for line in parser.get_input_lines():
    if not line:
        parse_board = False
        continue
    if parse_board:
        row = []
        for item in line:
            row.append(item)
        board_items.append(row)
    else:
        for item in line:
            movements.append(item)

board = build_board(board_items)
boxes_set = set()
board_set = set()
robot_position = (0, 0)
for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == '#':
            boxes_set.add((i, j))
        if board.items[i][j] == '@':
            robot_position = (i, j)
        board_set.add((i, j))

print(board)
print(movements)

movements_map = {
    '<': [(0, -1), (0, 1)],
    '>': [(0, 1), (0, -1)],
    '^': [(-1, 0), (1, 0)],
    'v': [(1, 0), (-1, 0)]
}

for movement in movements:
    direction_forward, direction_back = movements_map[movement]

    counter = 0

    next_position = robot_position
    dot_case = False
    while True:
        next_position = (next_position[0] + direction_forward[0], next_position[1] + direction_forward[1])

        if next_position in board_set and next_position not in boxes_set:
            counter += 1
            if board.items[next_position[0]][next_position[1]] == '.':
                dot_case = True
                break
        else:
            break

    if dot_case:
        last_position = next_position
        if not counter:
            raise Exception("Impossible case")
        for i in range(counter):
            next_edit_position = (last_position[0] + direction_back[0], last_position[1] + direction_back[1])
            board.items[last_position[0]][last_position[1]] = board.items[next_edit_position[0]][next_edit_position[1]]
            last_position = next_edit_position
        board.items[last_position[0]][last_position[1]] = '.'
        robot_position = (last_position[0] + direction_forward[0], last_position[1] + direction_forward[1])

    print(f'Move: {movement}')
    print(board)
    print('')

total = 0
for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == 'O':
            total += 100 * i + j

print(f'Total: {total}')
