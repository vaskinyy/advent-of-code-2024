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
wall_items = set()

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
        elif board.items[i][j] == '#':
            wall_items.add((i, j))


def find_shortest_path(board_coords):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = [(0, start_position, (0, 1), [start_position])]
    visited = defaultdict(lambda: 9999999)

    distances = []
    paths = []

    while queue:
        distance, current_cell, direction, path = heappop(queue)

        if current_cell == end_position:
            distances.append(distance)
            paths.append(path)
            continue

        if (current_cell, direction) in visited:
            continue

        visited[(current_cell, direction)] = distance

        possible_cells = [((current_cell[0] + item[0], current_cell[1] + item[1]), item) for item in directions]

        for (i, j), possible_direction in possible_cells:
            if (i, j) in board_coords:
                new_distance = distance + 1
                heappush(queue, (new_distance, (i, j), possible_direction, path + [(i, j)]))

    return distances, paths


distances, paths = find_shortest_path(initial_board_coords)
original_path_idx = distances.index(min(distances))
original_path_len = min(distances)
original_path = paths[original_path_idx]

print(original_path_len)

counter = 0
for start in range(len(original_path)):
    for end in range(start + 100, len(original_path)):
        distance = abs(original_path[start][0] - original_path[end][0]) + abs(
            original_path[start][1] - original_path[end][1])
        if end - start - distance >= 100 and distance <= 20:
            counter += 1

print(counter)
