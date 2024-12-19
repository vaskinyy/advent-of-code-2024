from collections import defaultdict
from functools import cache

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode, strip=False)
parser.parse()

parse_patterns = True

patterns = []
designs = []

for line in parser.get_input_lines():
    if not line:
        parse_patterns = False
        continue
    if parse_patterns:
        patterns = line.split(', ')
    else:
        designs.append(line)

print(patterns)
print(designs)
print(len(patterns))
print(len(designs))

cache = defaultdict(int)

num_cache_hits = 0


def pattern_is_possible(item):
    global num_cache_hits
    if item in cache:
        num_cache_hits += 1
        return cache[item]
    value = 0
    if not item:
        value = 1
    else:
        for pattern in patterns:
            if item.startswith(pattern):
                new_item = item.replace(pattern, '', 1)
                value += pattern_is_possible(new_item)
    cache[item] = value
    return value


counter = 0
for design in designs:
    val = pattern_is_possible(design)
    counter += val
print(counter)
# print(num_cache_hits)
