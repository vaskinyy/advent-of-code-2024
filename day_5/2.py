from functools import cmp_to_key

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

rules = set()
page_numbers = set()
items = []

for line in parser.get_input_lines():
    if '|' in line:
        rules.add(line)
        page_numbers.add(line.split('|')[0])
        page_numbers.add(line.split('|')[1])
    else:
        items.append(line.split(','))

incorrectly_ordered = []
for item in items:
    correct = True
    for i in range(len(item) - 1):
        if not correct:
            break
        for j in range(i + 1, len(item)):
            if f'{item[j]}|{item[i]}' in rules:
                correct = False
                break
    if not correct:
        incorrectly_ordered.append(item)

print(incorrectly_ordered)

corrected_items = []


def compare(item1, item2):
    if f'{item1}|{item2}' in rules:
        return -1
    elif f'{item2}|{item1}' in rules:
        return 1
    return 0


for item in incorrectly_ordered:
    corrected_items.append(sorted(item, key=cmp_to_key(compare)))

print(corrected_items)

sums = [int(item[len(item) // 2]) for item in corrected_items]
print(sums)
print(sum(sums))
