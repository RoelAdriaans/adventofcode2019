from adventofcode2019.solutions.day02 import Day02PartB


class TestDay02PartB:
    def test_day02b_data(self):
        """ Result we got when we did the real solution """
        solution = Day02PartB()
        res = solution("day_02/day02.txt")
        assert res == 7621
