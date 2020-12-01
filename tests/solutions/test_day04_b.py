import pytest

from adventofcode2019.solutions.day04 import Day04PartB


class TestDay04PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (112233, True),
            (123444, False),
            (111122, True),
            (111111, False),  # Probably false now?
            (223450, False),
            (123789, False),
            (1234, False),
        ],
    )
    def test_day04b_solve(self, input_data, expected_result):
        solution = Day04PartB()
        result = solution.is_valid_part_b(input_data)
        assert result == expected_result

    def test_day04b_data(self):
        """ Result we got when we did the real solution """
        solution = Day04PartB()
        res = solution("day_04/day04.txt")
        assert res != 453
        assert res != 583
        assert res != 624
        assert res != 70
        assert res != 74
        assert res == 677
