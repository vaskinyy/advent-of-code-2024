from copy import deepcopy

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

copy_board = deepcopy(board_items)
board_items = []

for i in range(len(copy_board)):
    row = []
    for j in range(len(copy_board[0])):
        if copy_board[i][j] == '#':
            row.append('#')
            row.append('#')
        elif copy_board[i][j] == '.':
            row.append('.')
            row.append('.')
        elif copy_board[i][j] == '@':
            row.append('@')
            row.append('.')
        elif copy_board[i][j] == 'O':
            row.append('[')
            row.append(']')
    board_items.append(row)

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


def move_sides(robot_position, direction_forward, direction_back):
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
        for _ in range(counter):
            next_edit_position = (last_position[0] + direction_back[0], last_position[1] + direction_back[1])
            board.items[last_position[0]][last_position[1]] = board.items[next_edit_position[0]][next_edit_position[1]]
            last_position = next_edit_position
        board.items[last_position[0]][last_position[1]] = '.'
        robot_position = (last_position[0] + direction_forward[0], last_position[1] + direction_forward[1])
    return robot_position


def move_up_down(robot_position, direction_forward, direction_back):
    next_position = (robot_position[0] + direction_forward[0], robot_position[1] + direction_forward[1])
    if board.items[next_position[0]][next_position[1]] not in ['[', ']']:
        robot_position = move_sides(robot_position, direction_forward, direction_back)
    else:
        visited = set()
        queue = [next_position]
        if board.items[next_position[0]][next_position[1]] == '[':
            queue.append((next_position[0], next_position[1] + 1))
        if board.items[next_position[0]][next_position[1]] == ']':
            queue.append((next_position[0], next_position[1] - 1))
        while queue:
            i, j = queue.pop(0)

            if (i, j) in visited:
                continue

            visited.add((i, j))

            next_position = (i + direction_forward[0], j + direction_forward[1])

            if board.items[next_position[0]][next_position[1]] == '[':
                queue.append(next_position)
                queue.append((next_position[0], next_position[1] + 1))
            elif board.items[next_position[0]][next_position[1]] == ']':
                queue.append(next_position)
                queue.append((next_position[0], next_position[1] - 1))

        has_move_space = True
        for (i, j) in visited:
            next_position = (i + direction_forward[0], j + direction_forward[1])
            if board.items[next_position[0]][next_position[1]] not in ['.', '[', ']']:
                has_move_space = False
                break
        if has_move_space:
            print('can move')
            visited = sorted([i for i in visited], key=lambda x: x[0],
                             reverse=True if direction_forward[0] == 1 else False)
            cache = {(i, j): board.items[i][j] for (i, j) in visited}
            for (i, j) in visited:
                next_position = (i + direction_forward[0], j + direction_forward[1])
                board.items[next_position[0]][next_position[1]] = cache[(i, j)]
                board.items[i][j] = '.'
            board.items[robot_position[0]][robot_position[1]] = '.'
            robot_position = (robot_position[0] + direction_forward[0], robot_position[1] + direction_forward[1])
            board.items[robot_position[0]][robot_position[1]] = '@'
    return robot_position


for movement in movements:
    direction_forward, direction_back = movements_map[movement]

    if movement in ['<', '>']:
        robot_position = move_sides(robot_position, direction_forward, direction_back)
    else:
        robot_position = move_up_down(robot_position, direction_forward, direction_back)

    print(f'Move: {movement}')
    print(board)
    print('')

total = 0
for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == '[':
            total += 100 * i + j

print(f'Total: {total}')
