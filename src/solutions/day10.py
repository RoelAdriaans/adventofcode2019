from utils.abstract import FileReaderSolution
from typing import List, NamedTuple, Set
import math


class Astroid(NamedTuple):
    x: int
    y: int


class Day10:
    astroids: List[Astroid]

    def create_map(self, input_data: str):
        """ Create a map from input_data. """
        self.astroids = []
        for y, line in enumerate(input_data.splitlines()):
            for x, point in enumerate(line):
                if point == "#":
                    self.astroids.append(Astroid(x=x, y=y))

    def _astroid_on_location(self, x: int, y: int) -> bool:
        """ Is there an astriod on  location (x, y) ?"""
        for astroid in self.astroids:
            if astroid.x == x and astroid.y == y:
                return True
        return False

    @staticmethod
    def _get_angle(astroid_1: Astroid, astroid_2: Astroid) -> float:
        """ Compute the angle between two Astroids in degrees """
        dx = astroid_1.x - astroid_2.x
        dy = astroid_1.y - astroid_2.y

        rads = math.atan2(dy, dx)
        degrees = math.degrees(rads)
        return degrees

    def count_asteroids_for_location(self, x: int, y: int) -> int:
        """
        Count how many astroids we can spot from this location.
        We do this by calculator the different angles we can see from this point.
        Duplicate angles are ignored.
        """
        found_angles: Set[float] = set()
        point_in_space = Astroid(x=x, y=y)

        for astroid in self.astroids:
            # Skip our own point
            if astroid.x == x and astroid.y == y:
                continue

            angle = self._get_angle(point_in_space, astroid)
            found_angles.add(angle)

        return len(found_angles)

    def find_best_spot(self) -> int:
        """Find the best spot to be in, and return how many astroids we can spot"""
        best_detected = max(
            self.count_asteroids_for_location(astroid.x, astroid.y)
            for astroid in self.astroids
        )

        return best_detected


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_map(input_data)
        best_detected = self.find_best_spot()
        return best_detected


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
