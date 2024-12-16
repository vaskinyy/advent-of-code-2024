from collections import defaultdict

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()

board = parser.get_board()

path_cells = set()
start_cell = (0, 0)
end_cell = (0, 0)

for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == '.':
            path_cells.add((i, j))
        elif board.items[i][j] == 'S':
            start_cell = (i, j)
        elif board.items[i][j] == 'E':
            end_cell = (i, j)
            path_cells.add((i, j))

direction = (0, 1)
turns = {
    (0, 1): [(1, 0), (-1, 0)],
    (1, 0): [(0, -1), (0, 1)],
    (0, -1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, 1), (0, -1)]
}

queue = [(start_cell, direction, 0)]
visited = defaultdict(lambda: 9999999)

distances = []

while queue:
    current_cell, direction, distance = queue.pop(0)

    if end_cell == current_cell:
        distances.append(distance)
        continue

    if current_cell in visited:
        if distance < visited[current_cell]:
            distance = min(distance, visited[current_cell])
        else:
            continue

    visited[current_cell] = distance

    possible_cells = [((current_cell[0] + item[0], current_cell[1] + item[1]), item) for item in turns[direction]]
    possible_cells.append(((current_cell[0] + direction[0], current_cell[1] + direction[1]), direction))

    for (i, j), possible_directions in possible_cells:
        if (i, j) in path_cells:
            new_distance = distance + (1 if possible_directions == direction else 1001)
            queue.append(((i, j), possible_directions, new_distance))
print(distances)
print(min(distances))
