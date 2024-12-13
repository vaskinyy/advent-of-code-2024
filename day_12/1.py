from models.board import get_coords_around_cross
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()
board = parser.get_board()
board_set = parser.get_board_set()


def get_region(start_i, start_j, board, visited):
    region = set()
    letter = board.items[start_i][start_j]
    queue = [(start_i, start_j)]

    while queue:
        i, j = queue.pop(0)

        if (i, j) in visited:
            continue
        visited.add((i, j))
        region.add((i, j))

        next_coords = get_coords_around_cross(i, j, board.height, board.width)
        for next_coord in next_coords:
            if board.items[next_coord[0]][next_coord[1]] == letter:
                queue.append((next_coord[0], next_coord[1]))

    return region, letter


visited = set()
region_letters = []

for i in range(board.height):
    for j in range(board.width):
        region, letter = get_region(i, j, board, visited)
        if region:
            region_letters.append((region, letter))
print(region_letters)

areas = [len(region) for region, _ in region_letters]
perimeters = []

for region, letter in region_letters:
    perimeter = 0
    for (i, j) in region:
        next_coords = get_coords_around_cross(i, j, board.height, board.width)
        perimeter += 4 - len(next_coords)
        for next_coord_i, next_coord_j in next_coords:
            if board.items[next_coord_i][next_coord_j] != letter:
                perimeter += 1
    perimeters.append(perimeter)

print(sum([area * perimeter for area, perimeter in zip(areas, perimeters)]))