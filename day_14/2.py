from models.board import get_coords_around_cross
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

robots = []

positions = []

for line in parser.get_input_lines():
    left, right = line.split(' ')
    pos_left, pos_right = left[2:].split(',')
    vel_left, vel_right = right[2:].split(',')
    robots.append((int(pos_right), int(pos_left), int(vel_right), int(vel_left)))
    positions.append((int(pos_right), int(pos_left)))

num_robots = len(robots)

width = 101
height = 103


def print_board(positions, width, height):
    print('-------------------')
    for i in range(height):
        for j in range(width):
            if (i, j) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print('')


def check_cluster(positions, width, height, counter):
    visited = set()

    for (i, j) in positions:
        queue = [(i, j)]
        region = set()
        while queue:
            item_i, item_j = queue.pop(0)

            if (item_i, item_j) in visited:
                continue

            visited.add((item_i, item_j))
            region.add((item_i, item_j))

            next_coords = get_coords_around_cross(item_i, item_j, height, width)
            for next_coord in next_coords:
                if (next_coord[0], next_coord[1]) in positions:
                    queue.append((next_coord[0], next_coord[1]))
        if region:
            if len(region) > 40:
                print(counter)
                print_board(positions, width, height)
    # print(counter)


counter = 0
while True:
    for idx, (_, _, vel_left, vel_right) in enumerate(robots):
        current_x, current_y = positions[idx]
        current_x, current_y = current_x + vel_left, current_y + vel_right
        if current_x < 0:
            current_x = height + current_x
        elif current_x >= height:
            current_x = current_x - height

        if current_y < 0:
            current_y = width + current_y
        elif current_y >= width:
            current_y = current_y - width

        positions[idx] = (current_x, current_y)
    counter += 1
    if counter > 8000:
        check_cluster(positions, width, height, counter)
