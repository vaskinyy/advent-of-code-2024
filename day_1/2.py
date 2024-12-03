from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

pairs = [[int(i) for i in item.split('   ')] for item in parser.get_input_lines()]

first_list = [item[0] for item in pairs]
second_list = [item[1] for item in pairs]

print(first_list)
print(second_list)


counts = []
for item in first_list:
    count = sum([1 if item == el else 0 for el in second_list])
    counts.append(count * item)
print(counts)
print(sum(counts))