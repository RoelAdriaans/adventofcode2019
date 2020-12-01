from adventofcode2019.solutions.day09 import Day09PartB


class TestDay09PartB:
    def test_day09b_data(self):
        """ Result we got when we did the real solution """
        solution = Day09PartB()
        res = solution("day_09/day09.txt")
        assert res == 78831
