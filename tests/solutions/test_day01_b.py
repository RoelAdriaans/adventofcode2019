import pytest

from adventofcode2019.solutions.day01 import Day01PartB


class TestDay01PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(14, 2), (1969, 966), (100756, 50346)],
    )
    def test_day01b_solve_module(self, input_data, expected_result):
        solution = Day01PartB()
        result = solution.compute_including_extra_fuel(input_data)
        assert result == expected_result

    def test_day01b_data(self):
        """ Result we got when we did the real solution """
        solution = Day01PartB()
        res = solution("day_01/day01.txt")
        assert res == 5194970
