import pytest

from adventofcode2019.solutions.day03 import Day03PartB


class TestDay03PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("R8,U5,L5,D3\nU7,R6,D4,L4", 30),
            (
                "R75,D30,R83,U83,L12,D49,R71,U7,L72\n"
                "U62,R66,U55,R34,D71,R55,D58,R83",
                610,
            ),
            (
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n"
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                410,
            ),
        ],
    )
    def test_day03b_solve(self, input_data, expected_result):
        solution = Day03PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day03b_data(self):
        """ Result we got when we did the real solution """
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 163676
