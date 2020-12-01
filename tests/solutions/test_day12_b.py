import pytest

from adventofcode2019.solutions.day12 import Day12PartB


class TestDay12PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                [
                    "<x=-1, y=0, z=2>",
                    "<x=2, y=-10, z=-7>",
                    "<x=4, y=-8, z=8>",
                    "<x=3, y=5, z=-1>",
                ],
                2_772,
            ),
            (
                [
                    "<x=-8, y=-10, z=0>",
                    "<x=5, y=5, z=10>",
                    "<x=2, y=-7, z=3>",
                    "<x=9, y=-8, z=-3>",
                ],
                4_686_774_924,
            ),
        ],
    )
    def test_day12b_solve(self, input_data, expected_result):
        input_string = "\n".join(input_data)
        solution = Day12PartB()
        result = solution.solve(input_string)
        assert result == expected_result

    def test_day12b_data(self):
        """ Result we got when we did the real solution """
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res == 467034091553512
