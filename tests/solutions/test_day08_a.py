from adventofcode2019.solutions.day08 import Day08PartA


class TestDay08PartA:
    def test_get_digits_per_layer(self):
        """ Get the number of digits per layer"""
        solution = Day08PartA()
        solution.load_image(image_data="123456789012", width=3, height=2)
        assert solution.frames[0] == "123456"
        assert solution.frames[1] == "789012"

        assert solution.count_number_per_frame(number=1, frame=0) == 1
        assert solution.count_number_per_frame(number=0, frame=1) == 1
        assert solution.count_number_per_frame(number=9, frame=0) == 0

    def test_layer_with_fewest_digit(self):
        """ Get the number of digits per layer"""
        solution = Day08PartA()

        solution.load_image(image_data="123451789012134161", width=3, height=2)
        assert solution.frames[0] == "123451"
        assert solution.frames[1] == "789012"
        assert solution.frames[2] == "134161"

        assert solution.layer_with_fewest_digit(1) == 1
        assert solution.layer_with_fewest_digit(3) == 1

    def test_day08a_data(self):
        """ Result we got when we did the real solution """
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 2904
