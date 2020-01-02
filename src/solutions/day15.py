from collections import defaultdict
from enum import IntEnum
from typing import List, Tuple, Union, NamedTuple, Dict
from time import sleep
from random import randint
from solutions.intcode import IntCode, ProgramFinished
from utils.abstract import FileReaderSolution
from utils.advent_utils import string_to_list_of_ints
from collections import deque, defaultdict


class Point(NamedTuple):
    x: int
    y: int


class Rotate(IntEnum):
    LEFT = 0
    RIGHT = 1


class Movement(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    @staticmethod
    def rotate(current_direction: "Movement", rotate_direction: Rotate) -> "Movement":
        """ Rotate the robot
        :param current_direction: Instance of Movement with current durection
        :param rotate_direction: Rotate: 0 Rotate left, 1 Rotate right
        """
        if rotate_direction == Rotate.RIGHT:
            turn_dict = {1: 4, 2: 3, 3: 1, 4: 2}
        elif rotate_direction == Rotate.LEFT:
            turn_dict = {1: 3, 2: 4, 3: 2, 4: 1}
        else:
            raise ValueError(f"Unknown rotateion {rotate_direction=}")

        new_direction = turn_dict[current_direction.value]
        return Movement(new_direction)

    @staticmethod
    def direction_update_x_y(current_direction: "Movement", point: Point) -> Point:
        """
        Update the coordinate if the movement succeeded

        :param current_direction: The current direction we're moving in
        :param point: Current position
        :return: Point) with new direction
        """
        if current_direction == Movement.NORTH:
            return Point(point.x, point.y - 1)
        elif current_direction == Movement.SOUTH:
            return Point(point.x, point.y + 1)
        elif current_direction == Movement.EAST:
            return Point(point.x + 1, point.y)
        elif current_direction == Movement.WEST:
            return Point(point.x - 1, point.y)
        else:
            raise ValueError(f"Invalid current direction {current_direction}")

    @staticmethod
    def get_opposite_direction(current_direction: "Movement"):
        """ Get the opposite direction

        North returns south, West returns east, ...
        """
        location_dict = {
            Movement.NORTH: Movement.SOUTH,
            Movement.SOUTH: Movement.NORTH,
            Movement.WEST: Movement.EAST,
            Movement.EAST: Movement.WEST,
        }

        new_direction = location_dict[current_direction.value]
        return Movement(new_direction)

DIRECTIONS = [Movement.NORTH, Movement.SOUTH, Movement.WEST, Movement.EAST]
ANTI_DIRECTIONS = [Movement.SOUTH, Movement.NORTH, Movement.EAST, Movement.WEST]
DELTAS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


class StatusCode(IntEnum):
    HIT_WALL = 0
    MOVE_REQUESTED = 1
    MOVE_REQUESTED_INSIDE = 2


class Tile(IntEnum):
    DROID = 0
    WALL = 1
    OPEN = 2
    OXYGEN = 3

    @staticmethod
    def show(tile):
        values = {
            Tile.DROID: "D",
            Tile.WALL: "#",
            Tile.OPEN: ".",
            Tile.OXYGEN: "*",
        }
        if tile in values:
            return values[tile]
        else:
            return " "


class Location:
    """ Location / Pixel in the maze """

    point: Point
    location_type: Tile

    def __init__(self, point: Point, location_type: Tile = None):
        self.point = point
        self.location_type = location_type

    def __repr__(self):
        tile = Tile.show(self.location_type)
        return f"({self.point} - {tile}"


class Day15:
    grid: Dict[Point, Location]
    paths: List[List[str]]

    def get_location(self, point: Point) -> Location:
        """ Get a locatino from the grid, or create a new location """
        if location := self.grid.get(point):
            return location
        else:
            new_location = Location(point=point)
            self.grid[point] = new_location
            return new_location

    def show_screen(self, droid_point: Point, direction: Union[bool, Movement]):
        """
        Draw the current grid on the console:
        """
        max_y = max([point.y for point in self.grid.keys()])
        max_x = max([point.x for point in self.grid.keys()])
        min_y = min([point.y for point in self.grid.keys()])
        min_x = min([point.x for point in self.grid.keys()])
        output = []
        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):
                point = Point(x, y)
                if y == droid_point.y and x == droid_point.x:
                    if direction == Movement.NORTH:
                        row.append("v")
                    elif direction == Movement.EAST:
                        row.append(">")
                    elif direction == Movement.SOUTH:
                        row.append("^")
                    elif direction == Movement.WEST:
                        row.append("<")
                    else:
                        row.append("D")
                else:
                    if point in self.grid:
                        row.append(Tile.show(self.grid[point].location_type))
                    else:
                        row.append(" ")
            output.append("".join(row))
        return "\n".join(output)

    def create_grid(self):
        self.grid = {}
        self.paths = []

    def run_robot(self, input_data: str):
        visited = {Point(0, 0)}

        inputs = deque([])

        def get_input() -> int:
            res = inputs.popleft()
            return res

        # computer = IntcodeComputer(PROGRAM, get_input)
        computer = IntCode()
        instructions = string_to_list_of_ints(input_data)
        computer.load_instructions(instructions)
        computer.set_input_function(get_input)

        frontier = deque([])
        frontier.append((computer.save(), 0, Point(0, 0)))

        while frontier:
            save_state, num_steps, point = frontier.popleft()
            computer.load(save_state)
            for direction, anti, (dx, dy) in zip(DIRECTIONS, ANTI_DIRECTIONS, DELTAS):
                inputs.append(direction.value)
                status = StatusCode(computer.run_return_or_raise())
                if status == StatusCode.MOVE_REQUESTED_INSIDE:
                    print("found oxygen after", num_steps + 1, "steps")
                    return num_steps + 1, computer
                elif status == StatusCode.HIT_WALL:
                    pass
                elif status == StatusCode.MOVE_REQUESTED:
                    new_loc = Point(point.x + dx, point.y + dy)
                    if new_loc not in visited:
                        visited.add(new_loc)
                        frontier.append((computer.save(), num_steps + 1, new_loc))
                        inputs.append(anti.value)
                        computer.run_return_or_raise()
                    else:
                        inputs.append(anti.value)
                        computer.run_return_or_raise()
        print("Nothing found?")


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_grid()
        steps, _ = self.run_robot(input_data)
        return steps


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
