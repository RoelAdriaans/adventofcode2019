from utils.abstract import FileReaderSolution
from utils.advent_utils import string_to_list_of_ints
from solutions.intcode import IntCode, ProgramFinished
from enum import IntEnum
from typing import NamedTuple
from collections import Counter, defaultdict


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
        """ Rotate the robot
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
    hull: defaultdict(int)

    def run_computer(self, input_data: str) -> int:
        instructions = string_to_list_of_ints(input_data)

        self.locations = Counter()
        self.hull = defaultdict(int)

        robot_1 = Robot()

        intcode = IntCode()
        intcode.load_instructions(instructions)

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
            return len(self.locations)


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run_computer(input_data)


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
