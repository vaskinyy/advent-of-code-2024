from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()

board = parser.get_board()

start_coord = None
board_coords = set()
obstacles = set()
for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == "^":
            start_coord = (i, j)
        if board.items[i][j] == "#":
            obstacles.add((i, j))
        board_coords.add((i, j))

visited = set()
direction = (-1, 0)

turn_map = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

while start_coord in board_coords:
    visited.add(start_coord)

    next_coord = (start_coord[0] + direction[0], start_coord[1] + direction[1])
    while next_coord in obstacles:
        direction = turn_map[direction]
        next_coord = (start_coord[0] + direction[0], start_coord[1] + direction[1])

    start_coord = next_coord
    print(len(visited))
print(len(visited))
