from adventofcode2019.solutions.day11 import Day11PartA, Direction, RotateDirection


class TestDay11PartA:
    def test_direction(self):
        direction = Direction.UP
        assert direction == Direction.UP

        direction = direction.rotate(RotateDirection.RIGHT)
        assert direction == Direction.RIGHT

        direction = direction.rotate(RotateDirection.RIGHT)
        assert direction == Direction.DOWN

        direction = direction.rotate(RotateDirection.LEFT)
        assert direction == Direction.RIGHT

        direction = direction.rotate(RotateDirection.LEFT)
        assert direction == Direction.UP

        direction = direction.rotate(RotateDirection.LEFT)
        assert direction == Direction.LEFT

    def test_day11a_data(self):
        """ Result we got when we did the real solution """
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res != 10601
        assert res != 39
        assert res == 2255
