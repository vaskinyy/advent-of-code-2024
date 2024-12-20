from collections import defaultdict
from heapq import heappop, heappush

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()

board = parser.get_board()

start_position = (0, 0)
end_position = (0, 0)
initial_board_coords = set()

for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == 'S':
            initial_board_coords.add((i, j))
            start_position = (i, j)
        elif board.items[i][j] == 'E':
            initial_board_coords.add((i, j))
            end_position = (i, j)
        elif board.items[i][j] == '.':
            initial_board_coords.add((i, j))


def find_shortest_path(board_coords):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = [(0, start_position, (0, 1))]
    visited = defaultdict(lambda: 9999999)

    distances = []

    while queue:
        distance, current_cell, direction = heappop(queue)

        if current_cell == end_position:
            distances.append(distance)
            continue

        if (current_cell, direction) in visited:
            continue

        visited[(current_cell, direction)] = distance

        possible_cells = [((current_cell[0] + item[0], current_cell[1] + item[1]), item) for item in directions]

        for (i, j), possible_direction in possible_cells:
            if (i, j) in board_coords:
                new_distance = distance + 1
                heappush(queue, (new_distance, (i, j), possible_direction))

    return min(distances)


original_path_len = find_shortest_path(initial_board_coords)
print(original_path_len)

cheat_coords = []

for i in range(board.height):
    j = 0
    while j < board.width:
        current_array = []
        k = j
        while k < board.width and len(current_array) < 4:
            if board.items[i][k] == 'S':
                current_array.append('.')
            elif board.items[i][k] == 'E':
                current_array.append('.')
            else:
                current_array.append(board.items[i][k])
            k += 1
            if current_array == ['.', '#', '#', '.']:
                cheat_coords.append([(i, k - 3), (i, k - 2)])
            if current_array == ['.', '#', '.']:
                cheat_coords.append([(i, k - 2)])
        current_array = []
        j += 1

for j in range(board.width):
    i = 0
    while i < board.height:
        current_array = []
        k = i
        while k < board.height and len(current_array) < 4:
            if board.items[k][j] == 'S':
                current_array.append('.')
            elif board.items[k][j] == 'E':
                current_array.append('.')
            else:
                current_array.append(board.items[k][j])
            k += 1
            if current_array == ['.', '#', '#', '.']:
                cheat_coords.append([(k - 3, j), (k - 2, j)])
            if current_array == ['.', '#', '.']:
                cheat_coords.append([(k - 2, j)])
        current_array = []
        i += 1

print(cheat_coords)
print(len(cheat_coords))

counter = 0
for (i, coords) in enumerate(cheat_coords):
    board_coords = initial_board_coords.copy()
    for coord in coords:
        board_coords.add(coord)

    new_shortest_path = find_shortest_path(board_coords)

    if new_shortest_path >= original_path_len:
        continue

    print(f'{i}: {len(cheat_coords)}')

    if original_path_len - new_shortest_path >= 100:
        counter += 1
print(counter)
