from collections import defaultdict

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

line = parser.get_input_lines()[0]

stones = [int(item) for item in line.split(' ')]


def get_new_stone_numbers(stone):
    stone_str = str(stone)
    new_stones = []
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
    return new_stones


blinks = 75

cache = defaultdict(int)
for stone in stones:
    cache[stone] += 1

for i in range(blinks):
    new_cache = defaultdict(int)

    for stone in cache:
        new_stone_numbers = get_new_stone_numbers(stone)
        for number in new_stone_numbers:
            new_cache[number] += cache[stone]
    cache = new_cache

print(sum(cache.values()))
