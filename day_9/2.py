from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

line = parser.get_input_lines()[0]
blocks = []
num_spaces = 0
counter = 0
is_number = True

empty_blocks = []
number_blocks = []

for item in line:
    number = int(item)
    start_idx = len(blocks)
    block_len = number
    for i in range(number):
        if is_number:
            blocks.append(counter)
        else:
            blocks.append('.')
            num_spaces += 1

    if is_number:
        number_blocks.append((start_idx, block_len, counter))
    else:
        empty_blocks.append((start_idx, block_len))
    if is_number:
        counter += 1

    is_number = not is_number
print(blocks)
print(num_spaces)

number_blocks = number_blocks[::-1]

while number_blocks:
    number_block = number_blocks.pop(0)
    number_block_start_idx, number_block_len, number_block_number = number_block
    current_empty_block_idx = 0
    while current_empty_block_idx < len(empty_blocks):
        empty_block_idx, empty_block_len = empty_blocks[current_empty_block_idx]
        if empty_block_idx > number_block_start_idx:
            break
        if number_block_len <= empty_block_len:
            for i in range(number_block_len):
                blocks[i + empty_block_idx] = number_block_number
                blocks[i + number_block_start_idx] = '.'
            if number_block_len == empty_block_len:
                empty_blocks.pop(current_empty_block_idx)
            else:
                empty_blocks[current_empty_block_idx] = (empty_block_idx + number_block_len,
                                                         empty_block_len - number_block_len)
            break
        current_empty_block_idx += 1

print(blocks)

sums = 0
for i, number in enumerate(blocks):
    if number == '.':
        continue
    sums += i * number
print(sums)
