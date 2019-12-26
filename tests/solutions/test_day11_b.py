from solutions.day11 import Day11PartB


class TestDay11PartB:
    def test_day11b_data(self):
        """ Result we got when we did the real solution """
        solution = Day11PartB()
        res = solution("day_11/day11.txt")
        assert res == "BCKFPCRA"
