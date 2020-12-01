import pytest

from adventofcode2019.solutions.day05 import Day05PartA


class TestDay05PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ([1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99]),
            ([1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]),
        ],
    )
    def test_day05a_test_new(self, input_data, expected_result):
        solution = Day05PartA()
        solution.instructions = input_data
        solution.process_instruction()
        assert solution.instructions == expected_result

    def test_day05a_data(self):
        """ Result we got when we did the real solution """
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res == 9431221
