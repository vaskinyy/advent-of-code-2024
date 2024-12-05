
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

rules = set()
items = []

for line in parser.get_input_lines():
    if '|' in line:
        rules.add(line)
    else:
        items.append(line.split(','))

correctly_ordered = []
for item in items:
    correct = True
    for i in range(len(item) - 1):
        if not correct:
            break
        for j in range(i + 1, len(item)):
            if f'{item[j]}|{item[i]}' in rules:
                correct = False
                break
    if correct:
        correctly_ordered.append(item)
print(correctly_ordered)

sums = [int(item[len(item) // 2]) for item in correctly_ordered]
print(sums)
print(sum(sums))