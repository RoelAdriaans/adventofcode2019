import pytest

from adventofcode2019.solutions.day16 import Day16PartB


class TestDay16PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("03036732577212944063491565474664", 84462026),
            ("02935109699940807407585447034323", 78725270),
            ("03081770884921959731165446850517", 53553731),
        ],
    )
    def test_day16b_solve(self, input_data, expected_result):
        solution = Day16PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16b_data(self):
        """ Result we got when we did the real solution """
        solution = Day16PartB()
        res = solution("day_16/day16.txt")
        assert res != 36468541
        assert res == 12064286
