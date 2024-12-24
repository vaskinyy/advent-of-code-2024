from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode, strip=False)
parser.parse()

parse_expressions = False

outputs = {}

expressions = {}

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

key = next(iter(expressions))
while expressions:
    val1, op, val2 = expressions[key]
    if val1 in outputs and val2 in outputs:
        if op == 'OR':
            outputs[key] = outputs[val1] or outputs[val2]
        elif op == 'AND':
            outputs[key] = outputs[val1] and outputs[val2]
        elif op == 'XOR':
            outputs[key] = outputs[val1] ^ outputs[val2]
        expressions.pop(key)
        if not expressions:
            break
        key = next(iter(expressions))
    elif val1 not in outputs:
        key = val1
    elif val2 not in outputs:
        key = val2

numbers_values = []

for item in outputs:
    if item.startswith('z'):
        numbers_values.append((int(item[1:]), outputs[item]))
val = 0


def set_bit(val, index, x):
    mask = 1 << index
    val &= ~mask
    if x:
        val |= mask
    return val

total = 0
for shift, val in numbers_values:
    total = set_bit(total, shift, val)
print(total)
