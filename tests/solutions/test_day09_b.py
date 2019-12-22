import pytest

from solutions.day09 import Day09PartB


class TestDay09PartB:
    @pytest.skip("Not yet implemented")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day09b_solve(self, input_data, expected_result):
        solution = Day09PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.skip("Not yet implemented")
    def test_day09b_data(self):
        """ Result we got when we did the real solution """
        solution = Day09PartB()
        res = solution("day_09/day09.txt")
        assert res == 0
