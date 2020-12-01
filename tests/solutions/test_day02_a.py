import pytest

from adventofcode2019.solutions.day02 import Day02PartA


class TestDay02PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("1,9,10,3,2,3,11,0,99,30,40,50", 3500),
            ("1,0,0,0,99", 2),
            ("2,3,0,3,99", 2),
            ("2,4,4,5,99,0", 2),
            ("1,1,1,4,99,5,6,0,99", 30),
        ],
    )
    def test_day02a_solve(self, input_data, expected_result):
        solution = Day02PartA()
        opcodes = [int(digit) for digit in input_data.split(",")]
        solution.load_instructions(opcodes)
        solution.run()
        result = solution.get_register(0)
        assert result == expected_result

    def test_day02a_data(self):
        """ Result we got when we did the real solution """
        solution = Day02PartA()
        res = solution("day_02/day02.txt")
        assert res == 3306701
