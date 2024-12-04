from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()
parser.build_boards()

board = parser.get_board()

patterns = [
    [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]],
    [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]],
    [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]],
    [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]]
]

counter = 0
for i in range(board.height - 2):
    for j in range(board.width - 2):
        for pattern in patterns:
            match = True
            for pattern_i in range(3):
                for pattern_j in range(3):
                    if pattern[pattern_i][pattern_j] == '.':
                        continue
                    if board.items[i+pattern_i][j+pattern_j] != pattern[pattern_i][pattern_j]:
                        match = False
                        break
            if match:
                counter += 1
                break
print(counter)


