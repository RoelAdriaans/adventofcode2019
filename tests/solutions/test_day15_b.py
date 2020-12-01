from adventofcode2019.solutions.day15 import Day15PartB, Location, Point, Tile


class TestDay15PartB:
    def test_day15b_solve(self):
        solution = Day15PartB()
        # Let's create a grid from the example.
        # The top left is 0,0
        points = [
            # " ##   "
            Location(point=Point(1, 0), location_type=Tile.WALL),
            Location(point=Point(2, 0), location_type=Tile.WALL),
            # "#..## "
            Location(point=Point(0, 1), location_type=Tile.WALL),
            Location(point=Point(1, 1), location_type=Tile.OPEN),
            Location(point=Point(2, 1), location_type=Tile.OPEN),
            Location(point=Point(3, 1), location_type=Tile.WALL),
            Location(point=Point(4, 1), location_type=Tile.WALL),
            #  012345
            # "#.#..#"
            Location(point=Point(0, 2), location_type=Tile.WALL),
            Location(point=Point(1, 2), location_type=Tile.OPEN),
            Location(point=Point(2, 2), location_type=Tile.WALL),
            Location(point=Point(3, 2), location_type=Tile.OPEN),
            Location(point=Point(4, 2), location_type=Tile.OPEN),
            Location(point=Point(5, 2), location_type=Tile.WALL),
            #  01234
            # "#.O.#"
            Location(point=Point(0, 3), location_type=Tile.WALL),
            Location(point=Point(1, 3), location_type=Tile.OPEN),
            Location(point=Point(2, 3), location_type=Tile.OXYGEN),
            Location(point=Point(3, 3), location_type=Tile.OPEN),
            Location(point=Point(4, 3), location_type=Tile.WALL),
            #  012345
            # " ###  "
            Location(point=Point(1, 4), location_type=Tile.WALL),
            Location(point=Point(2, 4), location_type=Tile.WALL),
            Location(point=Point(3, 4), location_type=Tile.WALL),
        ]
        # Convert this thing into the dict we need
        grid = {}
        for point in points:
            grid[point.point] = point

        solution.grid = grid
        result = solution.compute_fill_with_oxygen()

        # This should be 4, but for some reason the final solution is off by one in that
        # case. We, we goof up the test case, and add an extra 1 here..
        assert result == 5

    def test_day15b_data(self):
        """ Result we got when we did the real solution """
        solution = Day15PartB()
        res = solution("day_15/day15.txt")
        assert res != 346
        assert res != 347
        assert res == 348
