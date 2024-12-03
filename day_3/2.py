import re

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

sums = 0

num_donts = 0
num_dos = 0

enabled = True

for line in parser.get_input_lines():
    mul_pairs = []
    donts_indexes = []
    dos_indexes = []
    items = re.finditer(r'mul\(([0-9]+),([0-9]+)\)', line)
    for match in items:
        start_idx = match.start()
        pair = match.groups()
        mul_results = int(pair[0]) * int(pair[1])
        mul_pairs.append((start_idx, mul_results))

    items = re.finditer('do\(\)', line)
    for match in items:
        start_idx = match.start()
        dos_indexes.append((start_idx, -2))

    items = re.finditer("don\'t\(\)", line)
    for match in items:
        start_idx = match.start()
        donts_indexes.append((start_idx, -1))
    print(donts_indexes)
    print(dos_indexes)

    num_donts += len(donts_indexes)
    num_dos += len(dos_indexes)

    all_pairs = mul_pairs + dos_indexes + donts_indexes

    all_pairs = sorted(all_pairs, key=lambda x: x[0])
    print(all_pairs)

    for _, number in all_pairs:
        if number == -2:
            enabled = True
        elif number == -1:
            enabled = False
        else:
            if enabled:
                sums += number
print(sums)
print(num_donts)
print(num_dos)
