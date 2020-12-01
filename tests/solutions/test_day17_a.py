from collections import defaultdict

import pytest

from adventofcode2019.solutions.day17 import Day17PartA


class TestDay17PartA:
    @pytest.mark.skip("No longer required")
    def test_day17a_grid_to_lists(self):
        solution = Day17PartA()

        # fmt: off
        grid = [
            40, 50, 10,
            14, 15, 10,
            55, 66, 10,
        ]
        # fmt: on

        result = solution.grid_to_lists(grid)
        assert result == [[40, 50], [14, 15], [55, 66]]

    def test_day17a_grid(self, capsys):
        solution = Day17PartA()

        test_grid = [
            "..#..........\n",
            "..#..........\n",
            "#######...###\n",
            "#.#...#...#.#\n",
            "#############\n",
            "..#...#...#..\n",
            "..#####...^..\n",
        ]
        # Make grid as in the source: Convery ever charater to the int ascii value
        grid = defaultdict(dict)
        row = 0
        col = 0
        for x in "".join(test_grid):
            if x == "\n":
                # Newline
                row += 1
                col = 0
            else:
                grid[row][col] = ord(x)
                col += 1

        # Assert that our grid is valid, and that the print function works
        solution.print_grid(grid)
        captured = capsys.readouterr()
        assert captured.out == "".join(test_grid)

        # Find the markers
        markers = solution.compute_points(grid)
        assert len(markers) == 4
        assert (2, 2) in markers
        assert (4, 2) in markers
        assert (4, 6) in markers

        score = solution.compute_scores(markers)
        assert score == 76

    def test_day17a_data(self):
        """ Result we got when we did the real solution """
        solution = Day17PartA()
        res = solution("day_17/day17.txt")
        assert res == 5056
