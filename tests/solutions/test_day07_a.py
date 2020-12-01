import pytest

from adventofcode2019.solutions.day07 import Day07PartA


class TestDay07PartA:
    def test_day07a_for_sequence(self):
        instructinons = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        solution = Day07PartA()
        result = solution.compute_results_for_looped_sequence(
            instructinons, (4, 3, 2, 1, 0)
        )
        assert result == 43210

    @pytest.mark.parametrize(
        ("instructions", "expected_sequence", "expected_thrust"),
        [
            ("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0", "43210", 43210),
            (
                "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,"
                "23,23,1,24,23,23,4,23,99,0,0",
                "01234",
                54321,
            ),
            (
                "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,"
                "1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0",
                "10432",
                65210,
            ),
        ],
    )
    def test_day07a_solve(self, instructions, expected_sequence, expected_thrust):
        instructions = list(map(int, instructions.split(",")))
        solution = Day07PartA()
        sequence, thrust = solution.get_best_looped_sequence(0, 5, instructions)
        assert sequence == expected_sequence
        assert thrust == expected_thrust

    def test_day07a_data(self):
        """ Result we got when we did the real solution """
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 929800
