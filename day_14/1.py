from collections import defaultdict

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

robots = []

for line in parser.get_input_lines():
    left, right = line.split(' ')
    pos_left, pos_right = left[2:].split(',')
    vel_left, vel_right = right[2:].split(',')
    robots.append((int(pos_right), int(pos_left), int(vel_right), int(vel_left)))

final_positions = defaultdict(int)
width = 101
height = 103
seconds = 100

for pos_x, pos_y, vel_left, vel_right in robots:
    current_x, current_y = pos_x, pos_y
    for i in range(seconds):
        current_x, current_y = current_x + vel_left, current_y + vel_right
        if current_x < 0:
            current_x = height + current_x
        elif current_x >= height:
            current_x = current_x - height

        if current_y < 0:
            current_y = width + current_y
        elif current_y >= width:
            current_y = current_y - width

        print(current_x, current_y)
    final_positions[(current_x, current_y)] += 1


# final_positions = coordinates

def _count_in_boundaries(left_top_x, left_top_y, quad_width, quad_height, positions):

    total = 0
    for i in range(left_top_x, quad_height):
        for j in range(left_top_y, quad_width):
            # if i == x_middle or j == y_middle:
            #     continue
            if (i, j) in positions:
                total += positions[(i, j)]
    return total


top_left = _count_in_boundaries(0, 0, width // 2, height // 2, final_positions)
top_right = _count_in_boundaries(0, width // 2 + 1, width, height // 2, final_positions)
bottom_left = _count_in_boundaries(height // 2 + 1, 0, width // 2, height, final_positions)
bottom_right = _count_in_boundaries(height // 2 + 1, width // 2 + 1, width, height, final_positions)

print(final_positions)
print(top_left, top_right, bottom_left, bottom_right)
print(top_left * top_right * bottom_left * bottom_right)
