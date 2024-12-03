import re

from parasers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

sums = 0

for line in parser.get_input_lines():
    pattern = r'mul\(([0-9]+),([0-9]+)\)'
    items = re.findall(pattern, line)
    print(items)
    for (item1, item2) in items:
        sums += int(item1) * int(item2)
print(sums)
