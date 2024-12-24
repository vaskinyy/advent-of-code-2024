from collections import defaultdict

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode, strip=False)
parser.parse()

outputs = {}
expressions = {}
parse_expressions = False

for line in parser.get_input_lines():
    if not line:
        parse_expressions = True
        continue
    if not parse_expressions:
        left, right = line.split(': ')
        outputs[left] = int(right)
    else:
        left, right = line.split(' -> ')
        val1, op, val2 = left.split(' ')
        expressions[right] = (val1, op, val2)

for i in range(len(outputs)):
    for key in expressions:
        val1, op, val2 = expressions[key]
        if key not in outputs and val1 in outputs and val2 in outputs:
            if op == 'OR':
                outputs[key] = outputs[val1] or outputs[val2]
            elif op == 'AND':
                outputs[key] = outputs[val1] and outputs[val2]
            elif op == 'XOR':
                outputs[key] = outputs[val1] ^ outputs[val2]

input_items = defaultdict(set)
output_items = {}
initial_redirect = None

for key in expressions:
    val1, op, val2 = expressions[key]
    if {val1, op, val2} == {'x00', 'AND', 'y00'}:
        initial_redirect = key

    input_items[val1].add(op)
    input_items[val2].add(op)
    output_items[key] = (op, val1[1:].isnumeric())

target_nodes = []
for name in outputs:
    if name in ['z00', 'z45', initial_redirect]:
        continue
    if name[1:].isnumeric():
        if name.startswith('z') and output_items[name] != ('XOR', False):
            target_nodes.append(name)
        continue

    in_item = input_items[name]
    out_item = output_items[name]
    possible_items = [
        ({'OR'}, ('AND', True)),
        ({'AND', 'XOR'}, ('OR', False)),
        ({'OR'}, ('AND', False)),
        ({'AND', 'XOR'}, ('XOR', True)),
    ]
    if (in_item, out_item) not in possible_items:
        target_nodes.append(name)

items = ','.join(sorted(target_nodes))
print(items)
