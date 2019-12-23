import pytest

from solutions.day10 import Day10PartB, Astroid


class TestDay10PartB:
    def test_blowing_up_stuff(self):
        # The location of the X was 8,3
        initial_map = [
            ".#....#####...#..",
            "##...##.#####..##",
            "##...#...#.#####.",
            "..#.....#...###..",
            "..#.#.....#....##",
        ]
        single_line_map = "\n".join(initial_map)
        solution = Day10PartB()
        solution.create_map(single_line_map)

        # Check that we have an place
        best_spot = solution.get_best_astroid()[0]
        assert best_spot == Astroid(x=8, y=3)

        # We start going up:
        assert solution.laser_direction == 90

        first_one = solution.rotate_and_shoot_until_hit(best_spot)
        assert first_one == Astroid(x=8, y=1)

        shot = solution.rotate_and_shoot_until_hit(best_spot)
        assert shot == Astroid(x=9, y=0)

    def test_distance(self):
        # Problem wit distance during the test:
        location = Astroid(x=11, y=13)
        astroid_1 = Astroid(x=12, y=1)
        astroid_2 = Astroid(x=12, y=2)

        distance_1 = Day10PartB._get_distance(location, astroid_1)
        distance_2 = Day10PartB._get_distance(location, astroid_2)

        assert distance_1 < distance_2

    def test_day10b_big_map(self):
        input_map = [
            ".#..##.###...#######",
            "##.############..##.",
            ".#.######.########.#",
            ".###.#######.####.#.",
            "#####.##.#.##.###.##",
            "..#####..#.#########",
            "####################",
            "#.####....###.#.#.##",
            "##.#################",
            "#####.##.###..####..",
            "..######..##.#######",
            "####.##.####...##..#",
            ".#####..#.######.###",
            "##...#.##########...",
            "#.##########.#######",
            ".####.#.###.###.#.##",
            "....##.##.###..#####",
            ".#.#.###########.###",
            "#.#.#.#####.####.###",
            "###.##.####.##.#..##",
        ]
        single_line_map = "\n".join(input_map)
        solution = Day10PartB()
        solution.create_map(single_line_map)
        best_astroid, num_hits = solution.get_best_astroid()
        assert num_hits == 210
        assert best_astroid == Astroid(11, 13)
        solution.shoot_and_rotate(best_astroid, n=20)

        assert solution.astroids_destroyed[0] == Astroid(11, 12)  # 1th
        assert solution.astroids_destroyed[1] == Astroid(12, 1)  # 2 th
        assert solution.astroids_destroyed[2] == Astroid(12, 2)  # 3 th
        assert solution.astroids_destroyed[9] == Astroid(12, 2)  # 10th

    @pytest.mark.skip("Not get NotImplemented")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day10b_solve(self, input_data, expected_result):
        solution = Day10PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("Not get NotImplemented")
    def test_day10b_data(self):
        """ Result we got when we did the real solution """
        solution = Day10PartB()
        res = solution("day_10/day10.txt")
        assert res == 0
