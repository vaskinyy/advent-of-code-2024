from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode, strip=False)
parser.parse()

boards = []
new_board = []
for line in parser.get_input_lines():
    if not line:
        boards.append(new_board)
        new_board = []
        continue

    board_line = []
    for char in line:
        board_line.append(char)
    new_board.append(board_line)

pin_boards = []
key_boards = []

for board in boards:
    if set(board[0]) == {'.'}:
        key_boards.append(board)
    else:
        pin_boards.append(board)


def get_pin_counts(board, pin=True):
    counts = []
    for j in range(len(board[0])):
        count = -1
        iterator = range(len(board)) if pin else reversed(range(len(board)))
        for i in iterator:
            if board[i][j] == '#':
                count += 1
        counts.append(count)
    return counts


pin_counts = [get_pin_counts(board, pin=True) for board in pin_boards]
key_counts = [get_pin_counts(board, pin=False) for board in key_boards]

print(pin_counts)
print(key_counts)

total = 0
for pin_count in pin_counts:
    for key_count in key_counts:
        if all(key_count[i] + pin_count[i] <= 5 for i in range(5)):
            total += 1
print(total)
