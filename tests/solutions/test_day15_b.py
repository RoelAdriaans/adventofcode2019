import pytest

from solutions.day15 import Day15PartB


class TestDay15PartB:
    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day15b_solve(self, input_data, expected_result):
        solution = Day15PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day15b_data(self):
        """ Result we got when we did the real solution """
        solution = Day15PartB()
        res = solution("day_15/day15.txt")
        assert res == 0
