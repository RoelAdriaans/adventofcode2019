import pytest

from adventofcode2019.solutions.day05 import Day05PartB


class TestDay05PartB:
    def test_day05b_test_input_equal(self):
        solution = Day05PartB()

        # Position and immediate mode, is input equal to 8
        for data in (
            [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8],  # Position mode
            [3, 3, 1108, -1, 8, 3, 4, 3, 99],  # immediate
        ):
            solution.load_instructions(data)
            solution.load_input_values([8])
            res = solution.run()
            assert res == 1

            solution.load_instructions(data)
            solution.load_input_values([7])
            res = solution.run()
            assert res == 0

            solution.load_instructions(data)
            solution.load_input_values([9])
            res = solution.run()
            assert res == 0

        # Position and immediate mode, is len than 8
        for data in (
            [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8],  # Position mode
            [3, 3, 1107, -1, 8, 3, 4, 3, 99],  # Immediate mode
        ):
            solution.load_instructions(data)
            solution.load_input_values([8])
            res = solution.run()
            assert res == 0

            solution.load_instructions(data)
            solution.load_input_values([7])
            res = solution.run()
            assert res == 1

            solution.load_instructions(data)
            solution.load_input_values([9])
            res = solution.run()
            assert res == 0

        # Test jumps:
        # Here are some jump tests that take an input,
        # then output 0 if the input was zero or,
        # 1 if the input was non-zero:
        for data in (
            [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],  # Position Mode
            [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],  # Immediate mode
        ):

            solution.load_instructions(data)
            solution.load_input_values([0])
            res = solution.run()
            assert res == 0

            solution.load_instructions(data)
            solution.load_input_values([1])
            res = solution.run()
            assert res == 1

            solution.load_instructions(data)
            solution.load_input_values([150])
            res = solution.run()
            assert res == 1

    @pytest.mark.parametrize(
        ("input_value", "exoected_output_value"),
        [
            (4, 999),  # Output 999 when the input value is below 8
            (8, 1000),  # 1000 when the input value is equal to 8
            (10, 1001),  # 1001 if the value is greater then 8
        ],
    )
    def test_day05b_larger_example(self, input_value, exoected_output_value):
        instruction_data = (
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
            "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
            "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
        )
        instructions = list(map(int, instruction_data.split(",")))
        solution = Day05PartB()

        solution.load_instructions(instructions)
        solution.load_input_values([input_value])

        res = solution.run()
        assert res == exoected_output_value

    def test_day05b_data(self):
        """ Result we got when we did the real solution """
        solution = Day05PartB()
        res = solution("day_05/day05.txt")
        assert res == 1409363
