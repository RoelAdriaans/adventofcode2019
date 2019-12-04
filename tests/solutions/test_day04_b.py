import pytest

from solutions.day04 import Day04PartB


class TestDay04PartB:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day04b_solve(self, input_data, expected_result):
        solution = Day04PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day04b_data(self):
        """ Result we got when we did the real solution """
        solution = Day04PartB()
        res = solution("day_04/day04.txt")
        assert res == 0
