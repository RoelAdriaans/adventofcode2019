import pytest

from adventofcode2019.solutions.day07 import Day07PartB


class TestDay07PartB:
    @pytest.mark.parametrize(
        ("instructions", "expected_sequence", "expected_thrust"),
        [
            (
                "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,"
                "27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5",
                "98765",
                139629729,
            ),
            (
                "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,"
                "-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,"
                "53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10",
                "97856",
                18216,
            ),
        ],
    )
    def test_day07b_solve(self, instructions, expected_sequence, expected_thrust):
        instructions = list(map(int, instructions.split(",")))
        solution = Day07PartB()
        sequence, thrust = solution.get_best_looped_sequence(5, 10, instructions)
        assert sequence == expected_sequence
        assert thrust == expected_thrust

    def test_day07b_data(self):
        """ Result we got when we did the real solution """
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res == 15432220
