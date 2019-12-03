import pytest

from solutions.day03 import Day03PartB


class TestDay03PartB:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day03b_solve(self, input_data, expected_result):
        solution = Day03PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day03b_data(self):
        """ Result we got when we did the real solution """
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 0
