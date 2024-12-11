from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

line = parser.get_input_lines()[0]

stones = [int(item) for item in line.split(' ')]

blinks = 25

for i in range(blinks):
    new_stones = []

    for stone in stones:
        stone_str = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(stone_str) % 2 == 0:
            idx = len(stone_str) // 2
            left = stone_str[:idx]
            right = stone_str[idx:]
            new_stones.append(int(left))
            new_stones.append(int(right))
        else:
            new_stones.append(stone * 2024)

    stones = new_stones
print(len(stones))


