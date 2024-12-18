from collections import defaultdict
from heapq import heappop, heappush

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

size = 71
num_bytes = 1024

byte_list = []
board_coords = set()

for line in parser.get_input_lines():
    x, y = line.split(',')
    byte_list.append((int(y), int(x)))

bytes_set = set(byte_list[:num_bytes])

for i in range(size):
    for j in range(size):
        if (i, j) not in bytes_set:
            board_coords.add((i, j))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = [(0, (0, 0), (0, 1))]
visited = defaultdict(lambda: 9999999)

distances = []

while queue:
    distance, current_cell, direction = heappop(queue)

    if current_cell == (size - 1, size - 1):
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
print(distances)
print(min(distances))
