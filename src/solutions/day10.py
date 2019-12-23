from utils.abstract import FileReaderSolution
from typing import List, NamedTuple, Set, Tuple, Union
import math


class Astroid(NamedTuple):
    x: int
    y: int


class Day10:
    astroids: List[Astroid]
    astroids_destroyed: List[Astroid]

    # Our laser starts by pointing up
    laser_direction: float = 90

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

    @staticmethod
    def _get_distance(astroid_1: Astroid, astroid_2: Astroid) -> float:
        """ Compute the distance between two Astroids """
        a, b = astroid_1.x, astroid_1.y
        x, y = astroid_2.x, astroid_2.y
        res = abs(a - x) + abs(b - y)
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
        best_astroid = max(locations, key=locations.get)
        return best_astroid, locations[best_astroid]

    def run_laser(self, location: Astroid) -> Union[bool, Astroid]:
        """ Run the laser on map.
        `location` is the position we're on.
        Return false when no Astroid was hit, true otherwise
        """
        # First, find a target that is on the same degree:
        targets_in_range: Set[Astroid] = set()

        for astroid in self.astroids:
            angle = round(self._get_angle(location, astroid))
            if angle == self.laser_direction:
                targets_in_range.add(astroid)

        if not targets_in_range:
            return False

        # We can only shoot one target
        # Get the closest target
        distances = {
            astroid: self._get_distance(location, astroid)
            for astroid in targets_in_range
        }
        closest_target = min(distances, key=distances.get)

        # Let's kill this done!
        self.astroids_destroyed.append(closest_target)
        self.astroids.remove(closest_target)

        # Return the last one we've shot
        return closest_target

    def rotate_laser(self):
        """ Rotate the laser one degree """
        self.laser_direction += 1
        if self.laser_direction >= 361:
            self.laser_direction = 0

    def rotate_and_shoot_until_hit(self, location: Astroid):
        """ Shoot and rotate until we hit something """
        while True:
            hit_astroid = self.run_laser(location)
            # Always rotate laser after shooting, otherwise in the next try we hit
            # The astroid behing it
            self.rotate_laser()
            if hit_astroid:
                return hit_astroid

    def shoot_and_rotate(self, location: Astroid, n: int = 200):
        """ Shoot until we have reached `n` targets"""
        while len(self.astroids_destroyed) < n:
            self.run_laser(location=location)
            self.rotate_laser()
        return self.astroids_destroyed[n-1]


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_map(input_data)
        best_detected = self.find_best_spot()
        return best_detected


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
