import pytest

from adventofcode2019.solutions.day06 import Day06PartA


class TestDay06PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                [
                    "COM)B",
                    "B)C",
                    "C)D",
                    "D)E",
                    "E)F",
                    "B)G",
                    "G)H",
                    "D)I",
                    "E)J",
                    "J)K",
                    "K)L",
                ],
                42,
            )
        ],
    )
    def test_day06a_solve(self, input_data, expected_result):
        # Convert to format the solve routine expects
        input_data = "\n".join(input_data)
        solution = Day06PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day06a_data(self):
        """ Result we got when we did the real solution """
        solution = Day06PartA()
        res = solution("day_06/day06.txt")
        assert res != 1606
        assert res == 119831
