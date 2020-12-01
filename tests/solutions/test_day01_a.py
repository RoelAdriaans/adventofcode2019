import pytest

from adventofcode2019.solutions.day01 import Day01PartA


class TestDay01PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(12, 2), (14, 2), (1969, 654), (100756, 33583)],
    )
    def test_day01a_solve(self, input_data, expected_result):
        solution = Day01PartA()
        result = solution.compute_fuel(input_data)
        assert result == expected_result

    def test_day01a_data(self):
        """ Result we got when we did the real solution """
        solution = Day01PartA()
        res = solution("day_01/day01.txt")
        assert res == 3465245
