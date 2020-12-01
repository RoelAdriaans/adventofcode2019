from typing import List

from adventofcode2019.utils.abstract import FileReaderSolution


class Day08:
    frames: List[str]
    width = 0
    height = 0

    def load_image(self, image_data: str, width: int, height: int):
        """ Load an image from `image_data`, with `width` and `height` dimensions"""
        frame_size = width * height
        self.frames = [
            image_data[i : i + frame_size]
            for i in range(0, len(image_data), frame_size)
        ]

        self.width = width
        self.height = height

    def count_number_per_frame(self, number: int, frame: int) -> int:
        """ Count the number of times `number` is in frame `frame """
        needle = str(number)
        return self.frames[frame].count(needle)

    def layer_with_fewest_digit(self, number_to_find: int):
        """ Find the layer with the fewest corrences of `number_to_find` """
        found = {}
        for x in range(0, len(self.frames)):
            found[x] = self.count_number_per_frame(number=number_to_find, frame=x)
        return min(found, key=found.get)  # type: ignore

    @staticmethod
    def _compute_per_pixel(pixels: List[int]) -> int:
        for pixel in pixels:
            if pixel == 2:
                continue
            else:
                return pixel
        return 0

    def get_computed_image(self):
        """ Compute the image"""
        resulting_image = []
        for x in range(0, len(self.frames[0])):
            pixels = [int(frame[x]) for frame in self.frames]
            result = self._compute_per_pixel(pixels)
            resulting_image.append(result)
        return resulting_image

    def printable_image(self, image_data: List[int]):
        lines = [
            "".join(map(str, image_data[i : i + self.width]))
            for i in range(0, len(image_data), self.width)
        ]
        return "\n".join(lines)


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.load_image(input_data, width=25, height=6)
        # Find layer with the fewest 0 digits:
        layer = self.layer_with_fewest_digit(0)
        number_ones = self.count_number_per_frame(1, layer)
        number_twos = self.count_number_per_frame(2, layer)
        return number_ones * number_twos


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        self.load_image(input_data, width=25, height=6)
        image = self.get_computed_image()
        printable = self.printable_image(image)
        result = printable.replace("0", " ").replace("1", "■")
        return result
