import unittest

from day_17.task_1 import ProgramExecution, execute_program


class TestOperations(unittest.TestCase):
    def test_part_1(self):
        execution = ProgramExecution(program=[2, 6], output=[], register_c=9)
        execution = execute_program(execution, do_check=False)
        self.assertEqual(execution.register_b, 1)

    def test_part_2(self):
        execution = ProgramExecution(program=[5, 0, 5, 1, 5, 4], output=[], register_a=10)
        execution = execute_program(execution, do_check=False)
        self.assertEqual(execution.output, [0, 1, 2])

    def test_part_3(self):
        execution = ProgramExecution(program=[0, 1, 5, 4, 3, 0], output=[], register_a=2024)
        execution = execute_program(execution, do_check=False)
        self.assertEqual(execution.output, [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0])
        self.assertEqual(execution.register_a, 0)

    def test_part_4(self):
        execution = ProgramExecution(program=[1, 7], output=[], register_b=29)
        execution = execute_program(execution, do_check=False)
        self.assertEqual(execution.register_b, 26)

    def test_part_5(self):
        execution = ProgramExecution(program=[4, 0], output=[], register_b=2024, register_c=43690)
        execution = execute_program(execution, do_check=False)
        self.assertEqual(execution.register_b, 44354)
