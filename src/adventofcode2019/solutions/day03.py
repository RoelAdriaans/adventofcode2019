from typing import List

from adventofcode2019.utils.abstract import FileReaderSolution


class Point:
    x = 0
    y = 0
    steps = 0

    def __init__(self, x: int, y: int, steps: int = 0):
        """
        This class is a point in the grid.
        The steps parameter is optional and is ignored in the equality or hash
        checks.

        :param x: `x` location on the grid
        :param y: `y` location on the grid
        :param steps: Optional: Steps from the origin
        """
        self.x = x
        self.y = y
        self.steps = steps

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Day03:
    def __init__(self):
        self.lines = []

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
        steps = 1
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
                points.append(Point(x=posx, y=posy, steps=steps))
                value -= 1
                steps += 1
        return points

    def create_lines(self, input_lines: str):
        """ Create the lines and add them to the internal lines list """
        self.lines = []
        for line in input_lines.splitlines():
            self.lines.append(self.create_line(line))

    def find_duplicates(self):
        """ Find duplicates points in the internal lines list.  """
        common = list(set(self.lines[0]).intersection(self.lines[1]))
        return common

    def find_closest_point(self):
        """ Return the discance to the closest points in steps to reach it """
        duplicates = self.find_duplicates()
        # Get all the points, that are in
        total_distance = []
        for duplicate in duplicates:
            # Get all the points on this location
            points = [
                val for sublist in self.lines for val in sublist if val == duplicate
            ]
            # Add all the distances of these points together
            total_distance.append(sum(point.steps for point in points))

        return min(total_distance)

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
        min_distance = min(
            self.compute_distance(point_start, point) for point in common_coints
        )
        return min_distance


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_lines(input_data)
        return self.find_closest_point()
