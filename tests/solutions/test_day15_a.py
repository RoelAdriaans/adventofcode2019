import pytest

from solutions.day15 import Day15PartA, Movement, Point, Location


class TestDay15PartA:
    def test_movement(self):
        movement = Movement.NORTH

        assert movement.value == Movement.NORTH
        # Rotate Right
        movement = Movement.rotate(movement, 1)
        assert movement.value == Movement.EAST

        movement = Movement.rotate(movement, 1)
        assert movement.value == Movement.SOUTH

        movement = Movement.rotate(movement, 1)
        assert movement.value == Movement.WEST

        movement = Movement.rotate(movement, 1)
        assert movement.value == Movement.NORTH

        # And, the other way around!
        movement = Movement.rotate(movement, 0)
        assert movement.value == Movement.WEST
        movement = Movement.rotate(movement, 0)
        assert movement.value == Movement.SOUTH
        movement = Movement.rotate(movement, 0)
        assert movement.value == Movement.EAST
        movement = Movement.rotate(movement, 0)
        assert movement.value == Movement.NORTH

    def test_location(self):
        p1 = Point(1, 0)
        p2 = Point(2, 0)
        l1 = Location(point=p1)
        l2 = Location(point=p2)
        l1.set_edge(Movement.NORTH, l2)
        assert repr(l1) == "(Point(x=1, y=0) -   - edges: [Point(x=2, y=0)])"

    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day15a_solve(self, input_data, expected_result):
        solution = Day15PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day15a_data(self):
        """ Result we got when we did the real solution """
        solution = Day15PartA()
        res = solution("day_15/day15.txt")
        assert res == 228
