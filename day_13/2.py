from sympy import symbols, linsolve

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

items = []

lines = parser.get_input_lines()
i = 0
while i < len(lines):
    item = []
    for j in range(3):
        line = lines[i]
        i += 1

        _, right = line.split(": ")
        left, right = right.split(", ")
        item.append((int(left[2:]), int(right[2:])))
    items.append(item)
print(items)

total = 0
for item in items:
    xa, ya = item[0]
    xb, yb = item[1]
    xp, yp = item[2]

    a, b = symbols('a, b')

    results = linsolve([
        xa * a + xb * b - xp - 10000000000000,
        ya*a + yb*b - yp - 10000000000000
    ], (a, b))

    num_a, numb_b = next(iter(results))
    if '/' in str(num_a) or '/' in str(numb_b):
        continue
    total += num_a * 3 + numb_b
print(total)




