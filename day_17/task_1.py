from attrs import define

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()


@define
class ProgramExecution:
    register_a: int = 0
    register_b: int = 0
    register_c: int = 0
    index: int = 0
    program: list[int] = None
    output: list[int] = None

    def __repr__(self):
        return f'''
        Register A: {self.register_a}
        Register B: {self.register_b}
        Register C: {self.register_c}
        Index: {self.index}
        Output: {self.output}
        Program: {self.program}
        '''


execution = ProgramExecution(program=[], output=[])
for line in parser.get_input_lines():
    left, right = line.split(':')
    if left.startswith('Register A'):
        execution.register_a = int(right.strip())
    elif left.startswith('Register B'):
        execution.register_b = int(right.strip())
    elif left.startswith('Register C'):
        execution.register_c = int(right.strip())
    elif left.startswith('Program'):
        execution.program = [int(item) for item in right.strip().split(',')]

print(execution)


def get_literal_value(operand, value, execution):
    return value


def get_combo_value(operand, value, execution):
    if value in [0, 1, 2, 3]:
        return value
    if value == 4:
        return execution.register_a
    if value == 5:
        return execution.register_b
    if value == 6:
        return execution.register_c
    raise Exception(f'Wrong operand: {operand} {value} {execution}')


def adv_0(execution, do_check):
    stop = False
    operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 0:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1
    numerator = execution.register_a
    if execution.index >= len(execution.program) - 1:
        stop = True
    value = execution.program[execution.index]
    op_value = get_combo_value(operand, value, execution)
    denominator = pow(2, op_value)
    execution.register_a = numerator // denominator
    execution.index += 1
    return execution, stop


def bxl_1(execution, do_check):
    stop = False
    operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 1:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1

    val1 = execution.register_b

    if execution.index >= len(execution.program) - 1:
        stop = True

    value = execution.program[execution.index]
    op_value = get_literal_value(operand, value, execution)
    execution.index += 1

    execution.register_b = val1 ^ op_value

    return execution, stop


def bst_2(execution, do_check):
    stop = False
    operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 2:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1

    if execution.index >= len(execution.program) - 1:
        stop = True

    value = execution.program[execution.index]
    op_value = get_combo_value(operand, value, execution)

    execution.register_b = op_value % 8
    execution.index += 1

    return execution, stop


def jnz_3(execution, do_check):
    stop = False
    operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 3:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1

    if execution.index >= len(execution.program) - 1:
        stop = True

    value = execution.program[execution.index]
    op_value = get_literal_value(operand, value, execution)
    execution.index += 1

    if execution.register_a == 0:
        return execution, stop

    execution.index = op_value

    return execution, stop


def bxc_4(execution, do_check):
    stop = False
    # operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 4:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1

    if execution.index >= len(execution.program) - 1:
        stop = True
    execution.index += 1
    # value = execution.program[execution.index]
    # op_value = get_literal_value(operand, value, execution)

    execution.register_b = execution.register_b ^ execution.register_c

    return execution, stop


def bxc_5(execution, do_check):
    stop = False
    operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 5:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1

    if execution.index >= len(execution.program) - 1:
        stop = True

    value = execution.program[execution.index]
    op_value = get_combo_value(operand, value, execution)
    execution.index += 1

    execution.output.append(op_value % 8)

    return execution, stop


def bxc_6(execution, do_check):
    stop = False
    operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 6:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1
    numerator = execution.register_a
    if execution.index >= len(execution.program) - 1:
        stop = True

    value = execution.program[execution.index]
    op_value = get_combo_value(operand, value, execution)
    execution.index += 1
    denominator = pow(2, op_value)
    execution.register_b = numerator // denominator
    return execution, stop


def bxc_7(execution, do_check):
    stop = False
    operand = execution.program[execution.index]
    if do_check and execution.program[execution.index] != 7:
        raise Exception(f'Wrong execution: {execution}')
    execution.index += 1
    numerator = execution.register_a
    if execution.index >= len(execution.program) - 1:
        stop = True

    value = execution.program[execution.index]
    op_value = get_combo_value(operand, value, execution)
    execution.index += 1
    denominator = pow(2, op_value)
    execution.register_c = numerator // denominator
    return execution, stop


def execute_program(execution, do_check=True):
    steps = {
        0: adv_0,
        1: bxl_1,
        2: bst_2,
        3: jnz_3,
        4: bxc_4,
        5: bxc_5,
        6: bxc_6,
        7: bxc_7,

    }
    counter = 0
    while True:

        if execution.index >= len(execution.program):
            break
        step_function = steps[execution.program[execution.index]]
        execution, stop = step_function(execution, do_check)
        counter += 1
        print(f"Step {counter}")
        print(execution)
        # if stop:
        #     break

    return execution

execution = execute_program(execution, do_check=True)
print(execution)
print(','.join([str(item) for item in execution.output]))