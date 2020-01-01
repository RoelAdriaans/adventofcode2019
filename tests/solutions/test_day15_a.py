import pytest

from solutions.day15 import Day15PartA, Movement


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
        assert res == 0
