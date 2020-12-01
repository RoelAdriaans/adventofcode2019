from adventofcode2019.solutions.day13 import Day13PartA


class TestDay13PartA:
    def test_day13a_data(self):
        """ Result we got when we did the real solution """
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res == 205
