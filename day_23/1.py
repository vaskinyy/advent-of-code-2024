from collections import defaultdict
from itertools import combinations

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

pairs = [item.split('-') for item in parser.get_input_lines()]

connections = defaultdict(set)

for item1, item2 in pairs:
    connections[item1].add(item2)
    connections[item2].add(item1)

triplets = set()

for item in connections:
    target_set = connections[item].copy()
    target_set.add(item)

    items = combinations(target_set, 3)

    for item1, item2, item3 in items:
      item1_set = connections[item1]
      item2_set = connections[item2]
      item3_set = connections[item3]
      if (item2 in item1_set and item3 in item1_set
              and item1 in item2_set and item3 in item2_set
      and item1 in item3_set and item2 in item3_set):
          sorted_list = ','.join(sorted([item1, item2, item3]))
          triplets.add(sorted_list)

    # sorted_strings = (','.join(sorted(list(el))) for el in items)
    #
    # for string in sorted_strings:
    #     triplets.add(string)

counter = 0
for item in triplets:
    if any(el.startswith('t') for el in item.split(',')):
        counter += 1

print(triplets)
print(counter)