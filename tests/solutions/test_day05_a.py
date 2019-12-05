import pytest

from solutions.day05 import Day05PartA


class TestDay05PartA:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day05a_solve(self, input_data, expected_result):
        solution = Day05PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day05a_data(self):
        """ Result we got when we did the real solution """
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res == 0
