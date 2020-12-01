import pytest

from adventofcode2019.solutions.day04 import Day04PartA


class TestDay04PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(111111, True), (223450, False), (123789, False), (1234, False)],
    )
    def test_day04a_solve(self, input_data, expected_result):
        solution = Day04PartA()
        result = solution.is_valid_part_a(input_data)
        assert result == expected_result

    def test_day04a_data(self):
        """ Result we got when we did the real solution """
        solution = Day04PartA()
        res = solution("day_04/day04.txt")
        assert res != 246666
        assert res == 1048
