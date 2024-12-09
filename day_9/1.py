from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()


line = parser.get_input_lines()[0]
blocks = []
num_spaces = 0
counter = 0
is_number = True
for item in line:
    number = int(item)
    for i in range(number):
        if is_number:
            blocks.append(counter)
        else:
            blocks.append('.')
            num_spaces += 1
    if is_number:
        counter += 1

    is_number = not is_number
print(blocks)
print(num_spaces)

last_idx = len(blocks) - 1
current_idx = 0
while current_idx <= last_idx:
    while blocks[current_idx] != '.':
        current_idx += 1
    while blocks[last_idx] == '.':
        last_idx -= 1
    if current_idx > last_idx:
        break
    blocks[current_idx] = blocks[last_idx]
    blocks[last_idx] = '.'

print(blocks)

sums = 0
for i, number in enumerate(blocks):
    if number == '.':
        break
    sums += i*number
print(sums)