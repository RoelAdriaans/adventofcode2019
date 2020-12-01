from adventofcode2019.solutions.day13 import Day13PartB


class TestDay13PartB:
    def test_day13b_data(self):
        """ Result we got when we did the real solution """
        solution = Day13PartB()
        res = solution("day_13/day13.txt")
        assert res == 10292
