import pytest

from adventofcode2019.solutions.day10 import Astroid, Day10PartA


class TestDay10PartA:
    def test_read_map(self):
        map = [
            ".#..#",
            ".....",
            "#####",
            "....#",
            "...##",
        ]
        single_line_map = "\n".join(map)
        solution = Day10PartA()
        solution.create_map(single_line_map)
        assert len(solution.astroids) == 10
        assert solution.astroids[0] == Astroid(x=1, y=0)

    def test_get_angle(self):
        solution = Day10PartA()
        astroid_1 = Astroid(3, 4)  # Our base astroid
        astroid_2 = Astroid(2, 2)  # Astroid we can see
        astroid_3 = Astroid(1, 0)  # Astroid we should not be able to see

        # Test that both have the same angle, so astroid 3 will be behind and invisible
        # The actual unit doesn't matter, as long as we have the same units
        angle_1_2 = solution._get_angle(astroid_1, astroid_2)
        angle_1_3 = solution._get_angle(astroid_1, astroid_3)

        assert angle_1_2 == angle_1_3

        # Check the distance:
        distance_1_2 = solution._get_distance(astroid_1, astroid_2)
        distance_1_3 = solution._get_distance(astroid_1, astroid_3)

        # Validate that 1_3 is bigger then 1_2
        # Units to not mather, only distance
        assert distance_1_3 > distance_1_2

    @pytest.mark.parametrize(
        ("input_data", "best_location", "expected_result"),
        [
            ([".#..#", ".....", "#####", "....#", "...##"], (3, 4), 8),
            (
                [
                    "......#.#.",
                    "#..#.#....",
                    "..#######.",
                    ".#.#.###..",
                    ".#..#.....",
                    "..#....#.#",
                    "#..#....#.",
                    ".##.#..###",
                    "##...#..#.",
                    ".#....####",
                ],
                (5, 8),
                33,
            ),
        ],
    )
    def test_day10a_solve(self, input_data, best_location, expected_result):
        single_line_map = "\n".join(input_data)
        solution = Day10PartA()
        solution.create_map(single_line_map)
        count = solution.count_asteroids_for_location(
            x=best_location[0], y=best_location[1]
        )
        assert count == expected_result

        # Find the best place
        best_detected = solution.find_best_spot()
        assert best_detected == expected_result

        best_astroid, _ = solution.get_best_astroid()
        assert best_astroid == Astroid(x=best_location[0], y=best_location[1])

    def test_day10a_data(self):
        """ Result we got when we did the real solution """
        solution = Day10PartA()
        res = solution("day_10/day10.txt")
        assert res == 319
