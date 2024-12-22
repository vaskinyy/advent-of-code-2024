from functools import cache

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

numbers = [int(item) for item in parser.get_input_lines()]


def mix(value, secret_number):
    return value ^ secret_number


def prune(secret_number):
    return secret_number % 16777216


@cache
def get_next_number(secret_number):
    intermediate1 = mix(secret_number * 64, secret_number)
    secret_number1 = prune(intermediate1)

    intermediate2 = mix(secret_number1 // 32, secret_number1)
    secret_number2 = prune(intermediate2)

    intermediate3 = mix(secret_number2 * 2048, secret_number2)
    secret_number3 = prune(intermediate3)

    return secret_number3


total = 0

for number in numbers:
    for i in range(2000):
        number = get_next_number(number)
    total += number
print(total)
