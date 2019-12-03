from utils.abstract import FileReaderSolution
from collections import Counter, namedtuple
from typing import List

Point = namedtuple("Point", "x y")


class Day03:
    lines = None

    def __init__(self):
        self.lines = {}

    @staticmethod
    def create_line(input_str: str) -> List[Point]:
        """
        Create a line from the instructions in `input_str`.
        This function will return a List of `Point` namedtuples.
        `input_str` must be a comma seperated list of instructions in the format:
        LetterNumbers, where letter is in RUDN.
        Example "R20,U10,D9,L83"
        """
        points: List[Point] = []

        # start = Point(100, 100)
        # points.append(start)
        posx = 0
        posy = 0
        input_points = input_str.split(",")
        for point in input_points:
            value = int(point[1:])
            while value > 0:
                if point[0] == "R":
                    posx += 1
                elif point[0] == "U":
                    posy += 1
                elif point[0] == "D":
                    posy -= 1
                elif point[0] == "L":
                    posx -= 1
                points.append(Point(x=posx, y=posy))
                value -= 1
        return points

    def create_lines(self, input_lines: str):
        self.lines = []
        for line in input_lines.splitlines():
            self.lines.append(self.create_line(line))

    def find_duplicates(self):
        """ Find duplicates but remove """
        common = list(set(self.lines[0]).intersection(self.lines[1]))

        return common

    @staticmethod
    def compute_distance(point_a: Point, point_b: Point) -> int:
        """
        Compute the Manhattan distance between points (a, b) and (x, y)
        """
        a, b = point_a.x, point_a.y
        x, y = point_b.x, point_b.y
        res = abs(a - x) + abs(b - y)
        return res


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_lines(input_data)
        common_coints = self.find_duplicates()
        point_start = Point(0, 0)
        min_distance = min(self.compute_distance(point_start, point) for point in common_coints)
        return min_distance


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
