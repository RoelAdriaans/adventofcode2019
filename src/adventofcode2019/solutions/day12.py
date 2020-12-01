from itertools import combinations
from typing import List, Set, Tuple

import numpy as np  # type: ignore

from adventofcode2019.utils.abstract import FileReaderSolution


class Moon:
    # Position of the moon
    x: int
    y: int
    z: int

    # And the veloticy
    dx: int
    dy: int
    dz: int

    def __init__(self, x, y, z):
        self.dx, self.dy, self.dz = 0, 0, 0
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return (
            f"pos=<x={self.x:3}, y={self.y:3}, z={self.z:3}>, "
            f"vel=<x={self.dx:3}, y={self.dy:3}, z={self.dz:3}>"
        )

    def __eq__(self, other) -> bool:
        return (
            (self.x == other.x)
            and (self.y == other.y)
            and (self.z == other.z)
            and (self.dx == other.dx)
            and (self.dy == other.dy)
            and (self.dz == other.dz)
        )

    def apply_movement(self):
        """ Move the Moon according to the internal speeds """
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    @staticmethod
    def parse_input(input_str: str) -> "Moon":
        """Parse input string and return a moon

        Example input: <x=-1, y=0, z=2>
        """
        input_str = input_str.replace("<", "").replace(">", "")
        parts = input_str.split(",")
        moon_data = {}
        for part in parts:
            axis_part = part.split("=")
            moon_id = axis_part[0].strip()
            moon_data[moon_id] = int(axis_part[1])

        moon = Moon(**moon_data)
        return moon

    def get_potential_energy(self) -> int:
        """potential energy
        A moon's potential energy is the sum of the absolute values of its
        x, y, and z position coordinates
        :return:
        """
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinetic_energy(self) -> int:
        """A moon's kinetic energy is the sum of the absolute values of its velocity
         coordinates
        :return:
        """
        ...
        return abs(self.dx) + abs(self.dy) + abs(self.dz)

    def get_total_energy(self) -> int:
        """The total energy for a single moon is its potential energy multiplied by its
        kinetic energy."""
        return self.get_kinetic_energy() * self.get_potential_energy()


class Galaxy:
    moons: List[Moon]

    def __eq__(self, other) -> bool:
        return self.moons == other.moons

    def create_moons(self, input_str: str):
        self.moons = []
        lines = input_str.splitlines()
        for line in lines:
            moon = Moon.parse_input(line)
            self.moons.append(moon)

    @staticmethod
    def apply_gravity(moon1: Moon, moon2: Moon):
        """ Apply gravity to two pairs of moons. """
        for attribute in ("x", "y", "z"):
            dxattribute = f"d{attribute}"
            a1 = getattr(moon1, attribute)
            a2 = getattr(moon2, attribute)

            dxa1 = getattr(moon1, dxattribute)
            dxa2 = getattr(moon2, dxattribute)
            if a1 < a2:
                setattr(moon1, dxattribute, dxa1 + 1)
                setattr(moon2, dxattribute, dxa2 - 1)

            elif a1 > a2:
                setattr(moon1, dxattribute, dxa1 - 1)
                setattr(moon2, dxattribute, dxa2 + 1)

    def step(self):
        """ Step thru our system, one step at a time """
        # Look over two pairs of moons
        for pair in combinations(self.moons, 2):
            self.apply_gravity(pair[0], pair[1])

        # And then move the moons
        for moon in self.moons:
            moon.apply_movement()

    def step_multi(self, n: int):
        """ Do `n` steps """
        for _ in range(n):
            self.step()

    def get_total_energy(self) -> int:
        """ Return the total energy of all the Moons in the system"""
        return sum(moon.get_total_energy() for moon in self.moons)


class Day12:
    pass


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        galaxy = Galaxy()
        galaxy.create_moons(input_data)
        galaxy.step_multi(1000)
        return galaxy.get_total_energy()


class Day12PartB(Day12, FileReaderSolution):
    @staticmethod
    def return_one_var(galaxy: Galaxy, var: str) -> Tuple[int, ...]:
        """ Create a tuple with the Position and Velocity values for `var` """
        vardx = f"d{var}"
        values = tuple([getattr(moon, var) for moon in galaxy.moons]) + tuple(
            [getattr(moon, vardx) for moon in galaxy.moons]
        )
        return values

    def find_returning(self, galaxy: Galaxy, var: str) -> int:
        """Step over the galaxy movements until we find a position we seen before, for
        a single variable, `var`. This can be `x`, `y` or `z`.

        :return The number is steps it took before we reached the initial position
        """

        i = 0
        visited: Set[Tuple] = set()
        while True:
            values = self.return_one_var(galaxy, var)
            if values in visited:
                return i

            visited.add(values)
            galaxy.step()
            i += 1

    def solve(self, input_data: str) -> int:
        compare_galaxy = Galaxy()
        compare_galaxy.create_moons(input_data)

        galaxy = Galaxy()
        galaxy.create_moons(input_data)

        # Check the repeating values for X, Y, Z, for the position and the velocity
        repeating_x = self.find_returning(galaxy, "x")
        repeating_y = self.find_returning(galaxy, "y")
        repeating_z = self.find_returning(galaxy, "z")

        # Find the lowest common multiple for all the axis
        repeating = np.lcm.reduce([repeating_x, repeating_y, repeating_z])

        return repeating
