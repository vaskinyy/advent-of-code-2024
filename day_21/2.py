import itertools
from collections import defaultdict
from functools import cache

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

board_numbers = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['#', '0', 'A']
]

board_arrows = [
    ['#', '^', 'A'],
    ['<', 'v', '>']
]

codes = [line for line in parser.get_input_lines()]


@cache
def find_shortest_directions(start, end, board_type):
    boards = {
        'numbers': board_numbers,
        'arrows': board_arrows,
    }
    board = boards[board_type]
    start_idx = (0, 0)
    board_coords = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == start:
                start_idx = (i, j)
            if board[i][j] != '#':
                board_coords.add((i, j))

    queue = [(start_idx, (1, 0), [], 0)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    direction_paths = []

    visited = defaultdict(lambda: 99999)

    while queue:
        current_cell, current_direction, current_direction_paths, distance = queue.pop(0)

        if board[current_cell[0]][current_cell[1]] == end:
            direction_paths.append(current_direction_paths)
            continue

        if (current_cell, current_direction) in visited and visited[(current_cell, current_direction)] < distance:
            continue

        visited[(current_cell, current_direction)] = distance

        possible_cells = [((current_cell[0] + item[0], current_cell[1] + item[1]), item) for item in directions]

        for (i, j), possible_direction in possible_cells:
            if (i, j) in board_coords:
                new_distance = distance + 1
                queue.append(((i, j), possible_direction, current_direction_paths + [possible_direction], new_distance))

    shortest_length = 999999
    for i in range(len(direction_paths)):
        shortest_length = min(shortest_length, len(direction_paths[i]))
    shortest_paths = []
    for i in range(len(direction_paths)):
        if len(direction_paths[i]) == shortest_length:
            shortest_paths.append(direction_paths[i])

    return shortest_paths


directions_arrow = {
    (0, 1): '>',
    (0, -1): '<',
    (-1, 0): '^',
    (1, 0): 'v',
}


def get_min_len_item(items):
    shortest_length = 9999999999
    shortest_idx = 0
    for i in range(len(items)):
        shortest_length = min(shortest_length, len(items[i]))
        if shortest_length == len(items[i]):
            shortest_idx = i
    for i in range(len(items)):
        if i == shortest_idx:
            return items[i]


@cache
def generate_arrows_from_numbers(sequence):
    sequence = 'A' + sequence
    list_of_lists = []
    for i in range(len(sequence) - 1):
        current_paths = find_shortest_directions(sequence[i], sequence[i + 1], 'numbers')
        outputs = []
        for path in current_paths:
            output = []
            for direction in path:
                output.append(directions_arrow[direction])
            output.append('A')
            outputs.append(''.join(output))
        list_of_lists.append(outputs)

    products = list(itertools.product(*list_of_lists))
    return [list(item) for item in products]


@cache
def generate_arrows_from_arrows(sequence):
    list_of_lists = []
    sequence = 'A' + sequence

    for i in range(len(sequence) - 1):
        current_paths = find_shortest_directions(sequence[i], sequence[i + 1], 'arrows')
        outputs = []
        for path in current_paths:
            output = []
            for direction in path:
                output.append(directions_arrow[direction])
            output.append('A')
            outputs.append(''.join(output))
        list_of_lists.append(outputs)

    products = list(itertools.product(*list_of_lists))
    return [list(item) for item in products]


def code_to_number(code):
    while code.startswith('0'):
        code = code[1:]
    code = code[:-1]
    return int(code)


@cache
def get_min_len_instructions(code, num_layers):
    codes = generate_arrows_from_arrows(code)

    if num_layers == 1:
        return min([sum([len(code_item) for code_item in item]) for item in codes])

    return min([sum([get_min_len_instructions(code_item, num_layers - 1) for code_item in item]) for item in codes])


layers = 25
total = 0

for code in codes:
    current_code_sequences = generate_arrows_from_numbers(code)

    min_len = min([sum([get_min_len_instructions(code_item, layers) for code_item in item]) for item in
                   current_code_sequences])

    complexity = code_to_number(code) * min_len
    print(f'{min_len} * {code_to_number(code)}')
    total += complexity
print(total)
