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
sides_list = []


def _calculate_sides(sides_set):
    visited = set()
    regions = 0
    for (i, j) in sides_set:
        queue = [(i, j)]
        region = set()
        while queue:
            item_i, item_j = queue.pop(0)

            if (item_i, item_j) in visited:
                continue

            visited.add((item_i, item_j))
            region.add((item_i, item_j))

            next_coords = get_coords_around_cross(item_i, item_j, board.height, board.width)
            for next_coord in next_coords:
                if (next_coord[0], next_coord[1]) in sides_set:
                    queue.append((next_coord[0], next_coord[1]))
        if region:
            regions += 1
    return regions


for region, letter in region_letters:
    side_sets = [set(), set(), set(), set()]
    sides = 0

    # left
    for (i, j) in region:
        if j - 1 < 0 or board.items[i][j - 1] != letter:
            side_sets[0].add((i, j))

    # up
    for (i, j) in region:
        if i - 1 < 0 or board.items[i - 1][j] != letter:
            side_sets[1].add((i, j))

    # right
    for (i, j) in region:
        if j + 1 >= board.width or board.items[i][j + 1] != letter:
            side_sets[2].add((i, j))

    # down
    side_set = set()
    for (i, j) in region:
        if i + 1 >= board.height or board.items[i + 1][j] != letter:
            side_sets[3].add((i, j))

    calculated_sides = [_calculate_sides(item) for item in side_sets]
    sides_list.append(sum(calculated_sides))

print(sides_list)
print(sum([area * perimeter for area, perimeter in zip(areas, sides_list)]))
