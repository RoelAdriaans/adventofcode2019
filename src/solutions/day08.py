from utils.abstract import FileReaderSolution
from utils.advent_utils import string_to_list_of_ints


class Day08:
    frames = []

    def load_image(self, image_data: str, width: int, height: int):
        """ Load an image from `image_data`, with `width` and `height` dimensions"""
        frame_size = width * height
        self.frames = [
            image_data[i : i + frame_size]
            for i in range(0, len(image_data), frame_size)
        ]

    def count_number_per_frame(self, number: int, frame: int) -> int:
        """ Count the number of times `number` is in frame `frame """
        number = str(number)
        return self.frames[frame].count(number)

    def layer_with_fewest_digit(self, number_to_find: int):
        """ Find the layer with the fewest corrences of `number_to_find` """
        found = {}
        for x in range(0, len(self.frames)):
            found[x] = self.count_number_per_frame(number=number_to_find, frame=x)
        return min(found, key=found.get)


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.load_image(input_data, width=25, height=6)
        # Find layer with the fewest 0 digits:
        layer = self.layer_with_fewest_digit(0)
        number_ones = self.count_number_per_frame(1, layer)
        number_twos = self.count_number_per_frame(2, layer)
        return number_ones * number_twos


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
