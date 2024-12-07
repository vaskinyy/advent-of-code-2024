import math

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

items_pairs = []

for line in parser.get_input_lines():
    left, right = line.split(': ')
    items_pairs.append((int(left), [int(item) for item in right.split(' ')]))

possible_numbers = []

print(len(items_pairs))

for number, items in items_pairs:
    places = len(items) - 1

    partial_sums = [(math.prod, 0, 0), (math.fsum, 0, 0)]

    while partial_sums:
        sign_func, partial_sum, start_ids = partial_sums.pop(0)
        left = items[start_ids] if start_ids == 0 else partial_sum
        new_partial_sum = sign_func([left, items[start_ids + 1]])
        if start_ids == len(items) - 2:
            if new_partial_sum == number:
                possible_numbers.append(number)
                break
            continue
        if partial_sum < number:
            partial_sums.append((math.prod, new_partial_sum, start_ids + 1))
            partial_sums.append((math.fsum, new_partial_sum, start_ids + 1))

print(possible_numbers)
print(sum(possible_numbers))
