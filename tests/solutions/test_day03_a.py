import pytest

from adventofcode2019.solutions.day03 import Day03PartA, Point


class TestDay03PartA:
    def test_day03a_point(self):
        point_a = Point(x=10, y=42)
        point_b = Point(x=10, y=42)
        point_q = Point(x=11, y=42)

        assert point_a == point_b
        assert point_a != point_q

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("R8", 8), ("R8,U5", 13)]
    )
    def test_day03a_create(self, input_data, expected_result):
        solution = Day03PartA()
        result = solution.create_line(input_data)
        assert len(result) == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("R8,U5,L5,D3\nU7,R6,D4,L4", 6),
            (
                "R75,D30,R83,U83,L12,D49,R71,U7,L72\n"
                "U62,R66,U55,R34,D71,R55,D58,R83",
                159,
            ),
            (
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n"
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                135,
            ),
        ],
    )
    def test_day03a_solve(self, input_data, expected_result):
        solution = Day03PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day03a_data(self):
        """ Result we got when we did the real solution """
        solution = Day03PartA()
        res = solution("day_03/day03.txt")
        assert res == 8015
