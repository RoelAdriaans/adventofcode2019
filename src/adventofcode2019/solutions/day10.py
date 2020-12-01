import math
from collections import defaultdict
from typing import Dict, List, NamedTuple, Set, Tuple

from adventofcode2019.utils.abstract import FileReaderSolution


class Astroid(NamedTuple):
    x: int
    y: int


class GridInfo(NamedTuple):
    astroid: Astroid
    angle: float
    distance: float


class Day10:
    astroids: List[Astroid]
    astroids_destroyed: List[Astroid]

    def create_map(self, input_data: str):
        """ Create a map from input_data. """
        self.astroids = []
        self.astroids_destroyed = []
        for y, line in enumerate(input_data.splitlines()):
            for x, point in enumerate(line):
                if point == "#":
                    self.astroids.append(Astroid(x=x, y=y))
                elif point == "X":
                    print(x, y)

    @staticmethod
    def _get_angle(astroid_1: Astroid, astroid_2: Astroid) -> float:
        """ Compute the angle between two Astroids in degrees """
        dx = astroid_1.x - astroid_2.x
        dy = astroid_1.y - astroid_2.y

        rads = math.atan2(dy, dx)
        degrees = math.degrees(rads)
        return degrees

    @staticmethod
    def _get_distance(astroid_1: Astroid, astroid_2: Astroid) -> float:
        """ Compute the distance between two Astroids """
        a, b = astroid_1.x, astroid_1.y
        x, y = astroid_2.x, astroid_2.y
        euclidean_distance = math.sqrt((a - x) ** 2 + (b - y) ** 2)
        return euclidean_distance

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
        return self.get_best_astroid()[1]

    def get_best_astroid(self) -> Tuple[Astroid, int]:
        """ Return the best astroid location and the number of visable astroids"""
        locations = {
            astroid: self.count_asteroids_for_location(astroid.x, astroid.y)
            for astroid in self.astroids
        }
        best_astroid = max(locations, key=locations.get)  # type: ignore
        return best_astroid, locations[best_astroid]

    def calculate_angles(self, location: Astroid):
        """ Create a dict with all the angles for the asteroids and the distance"""
        angles: Dict[float, List] = defaultdict(list)
        for astroid in self.astroids:
            angle = self._get_angle(location, astroid)
            distance = self._get_distance(location, astroid)
            info = GridInfo(astroid=astroid, angle=angle, distance=distance)
            angles[angle].append(info)
        return angles

    def remove_astroid(self, location: Astroid, n=200):
        """ Shoot until we have reached `n` targets"""
        angle_information = self.calculate_angles(location)
        sorted_angles = sorted(angle_information)

        # We start at index with 90 degrees
        start_pos = sorted_angles.index(90)
        angles = sorted_angles[start_pos:] + sorted_angles[:start_pos]
        while len(self.astroids_destroyed) <= n:
            for angle in angles:
                # Get the closest in this angle
                astroids = angle_information[angle]
                if astroids:
                    closest = min(astroids, key=lambda x: x.distance)
                    astroids.remove(closest)
                    self.astroids_destroyed.append(closest.astroid)


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_map(input_data)
        best_detected = self.find_best_spot()
        return best_detected


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_map(input_data)
        best_astroid, num_hits = self.get_best_astroid()
        self.remove_astroid(best_astroid, n=200)
        astroid_destroied = self.astroids_destroyed[199]

        return astroid_destroied.x * 100 + astroid_destroied.y
