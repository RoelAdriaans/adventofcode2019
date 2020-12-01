import pytest

from adventofcode2019.solutions.day06 import Day06PartB


class TestDay06PartB:
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
                    "K)YOU",
                    "I)SAN",
                ],
                4,
            )
        ],
    )
    def test_day06b_solve(self, input_data, expected_result):
        # Convert to format the solve routine expects
        input_data = "\n".join(input_data)
        solution = Day06PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day06b_data(self):
        """ Result we got when we did the real solution """
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 322
