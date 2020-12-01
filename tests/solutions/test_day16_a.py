import pytest

from adventofcode2019.solutions.day16 import Day16PartA


class TestDay16PartA:
    @pytest.mark.parametrize(
        ("num_digits", "multiplier", "expected_result"),
        [
            (8, 1, [1, 0, -1, 0, 1, 0, -1, 0]),
            (8, 2, [0, 1, 1, 0, 0, -1, -1, 0]),
        ],
    )
    def test_day16_generate_pattern(self, num_digits, multiplier, expected_result):
        solution = Day16PartA()
        assert (
            solution.generate_pattern(num_digits=num_digits, multiplier=multiplier)
            == expected_result
        )

    def test_day16a_single_pattern(self):
        solution = Day16PartA()
        run_1 = solution.run_phases([1, 2, 3, 4, 5, 6, 7, 8], 1)
        assert run_1 == [4, 8, 2, 2, 6, 1, 5, 8]

        run_2 = solution.run_phases(run_1, 1)
        assert run_2 == [3, 4, 0, 4, 0, 4, 3, 8]

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("80871224585914546619083218645595", 24176176),
            ("19617804207202209144916044189917", 73745418),
            ("69317163492948606335995924319873", 52432133),
        ],
    )
    def test_day16a_solve(self, input_data, expected_result):
        solution = Day16PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16a_data(self):
        """ Result we got when we did the real solution """
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 28430146
