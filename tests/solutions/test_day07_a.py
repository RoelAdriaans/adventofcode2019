import pytest
from pathlib import Path
from solutions.intcode import IntCode
from solutions.day07 import Day07PartA

root_dir = Path(__file__).parent.parent.parent


class TestDay07PartA:
    @pytest.mark.parametrize(
        ("instructions", "expected_result"),
        [
            ("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0", "43210"),
            (
                "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,"
                "23,23,1,24,23,23,4,23,99,0,0",
                "54321",
            ),
        ],
    )
    def test_day07a_solve(self, instructions, expected_result):
        instructions = list(map(int, instructions.split(",")))
        solution = Day07PartA()
        sequence, result = solution.get_best_sequence(instructions)
        assert result == expected_result

    def test_day07a_data(self):
        """ Result we got when we did the real solution """
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 0
