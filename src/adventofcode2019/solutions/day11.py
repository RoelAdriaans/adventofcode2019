from collections import Counter, defaultdict
from enum import IntEnum
from typing import NamedTuple

import matplotlib.pyplot as plt  # type: ignore

from adventofcode2019.solutions.intcode import IntCode, ProgramFinished
from adventofcode2019.utils.abstract import FileReaderSolution
from adventofcode2019.utils.advent_utils import string_to_list_of_ints


class Location(NamedTuple):
    """
     X -->
    Y
    |
    |
    V
    """

    x: int
    y: int


class RotateDirection(IntEnum):
    LEFT = 0
    RIGHT = 1


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def rotate(self, rotate_direction: RotateDirection) -> "Direction":
        """Rotate the robot
        :param
        :param rotate_direction: Rotate: 0 Rotate left, 1 Rotate right
        """
        if rotate_direction == RotateDirection.RIGHT:
            new_direction = (self + 1) % 4
        elif rotate_direction == RotateDirection.LEFT:
            new_direction = (self - 1) % 4
        else:
            raise ValueError(f"Unknown direction {rotate_direction}")
        return Direction(new_direction)


class Robot:
    current_direction: Direction
    current_location: Location

    def __init__(self):
        self.current_location = Location(0, 0)
        self.current_direction = Direction.UP

    def walk(self):
        """
        Walk and return the new location of our robot.
        X is Horizontal, Y is vertical

        """
        if self.current_direction == Direction.UP:
            self.current_location = Location(
                self.current_location.x, self.current_location.y + 1
            )

        elif self.current_direction == Direction.DOWN:
            self.current_location = Location(
                self.current_location.x, self.current_location.y - 1
            )

        elif self.current_direction == Direction.RIGHT:
            self.current_location = Location(
                self.current_location.x + 1, self.current_location.y
            )

        elif self.current_direction == Direction.LEFT:
            self.current_location = Location(
                self.current_location.x - 1, self.current_location.y
            )


class Day11:
    locations: Counter
    hull: defaultdict

    def run_computer(self, input_data: str, start_color: int) -> int:
        instructions = string_to_list_of_ints(input_data)

        self.locations = Counter()
        self.hull = defaultdict(int)

        robot_1 = Robot()

        intcode = IntCode()
        intcode.load_instructions(instructions)

        # Set a starting color
        self.hull[robot_1.current_location] = start_color

        try:
            while True:
                current_color = self.hull[robot_1.current_location]

                intcode.load_input_values([current_color])
                # First result will be the color
                color_result = intcode.run_return_or_raise()
                direction_result = intcode.run_return_or_raise()

                self.hull[robot_1.current_location] = color_result
                self.locations[robot_1.current_location] += 1

                robot_1.current_direction = robot_1.current_direction.rotate(
                    RotateDirection(direction_result)
                )
                robot_1.walk()
        except ProgramFinished:
            return True


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.run_computer(input_data, start_color=0)
        return len(self.locations)


class Day11PartB(Day11, FileReaderSolution):
    def plot_grid(self):
        """ Plot the grid using matplotlib"""
        x_points = [point.x for point, color in self.hull.items()]
        y_points = [point.y for point, color in self.hull.items()]
        min_x = min(x_points)
        min_y = min(y_points)

        for point, color in self.hull.items():
            if color == 1:
                point_x = point.x + abs(min_x)
                point_y = point.y + abs(min_y)
                plt.scatter(point_x, point_y, c="black")
        plt.ylabel("some numbers")
        plt.show()

    def show(self):
        """ Plot the grid using Ascii"""
        positions = [
            (point.x, point.y) for point, color in self.hull.items() if color == 1
        ]
        x_min = min(x for (x, y) in positions)
        x_max = max(x for (x, y) in positions)
        y_min = min(y for x, y in positions)
        y_max = max(y for x, y in positions)

        output = []
        for y in reversed(range(y_min, y_max + 1)):
            row = ["░" if (x, y) in positions else " " for x in range(x_min, x_max + 1)]
            output.append("".join(row))
        return "\n".join(output)

    def solve(self, input_data: str) -> str:
        self.run_computer(input_data, start_color=1)
        return self.show()
