from collections import defaultdict
from enum import IntEnum
from typing import List, Tuple, Union, NamedTuple, Dict
from time import sleep

from solutions.intcode import IntCode, ProgramFinished
from utils.abstract import FileReaderSolution
from utils.advent_utils import string_to_list_of_ints


class Point(NamedTuple):
    x: int
    y: int


class Movement(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    @staticmethod
    def rotate(current_direction: "Movement", rotate_direction: int) -> "Movement":
        """ Rotate the robot
        :param current_direction: Instance of Movement with current durection
        :param rotate_direction: Rotate: 0 Rotate left, 1 Rotate right
        """
        if rotate_direction == 1:
            turn_dict = {1: 4, 2: 3, 3: 1, 4: 2}
        else:
            turn_dict = {1: 3, 2: 4, 3: 2, 4: 1}

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
        instructions = string_to_list_of_ints(input_data)
        intcode = IntCode()
        current_direction = Movement.NORTH
        path = []
        locations_visited = set()
        counter = 0

        def return_input():
            # Implement Dijkstra's thing here. Or, only when we have the grid
            print(f"Returning input: {current_direction} ({current_direction.value})")
            return current_direction.value

        intcode.set_input_function(return_input)
        intcode.load_instructions(instructions)
        # Current location of the bot:
        point = Point(0, 0)
        current_location = self.get_location(point)
        current_location.location_type = Tile.OPEN
        # First, Let's see if we can build anything
        try:
            while True:
                result = intcode.run_return_or_raise()
                status = StatusCode(result)
                if status == StatusCode.HIT_WALL:
                    # The position we tried to move into was a wall:
                    wall_point = Movement.direction_update_x_y(current_direction, point)
                    wall_location = self.get_location(wall_point)
                    wall_location.location_type = Tile.WALL

                elif status == StatusCode.MOVE_REQUESTED:
                    point = Movement.direction_update_x_y(current_direction, point)
                    location = self.get_location(point)
                    location.location_type = Tile.OPEN

                    path.append(location)
                    locations_visited.add(point)

                elif status == StatusCode.MOVE_REQUESTED_INSIDE:
                    self.grid[point].location_type = Tile.OXYGEN
                    path.append(point)
                    locations_visited.add(point)
                    return

                sleep(0.8)
                print(chr(27) + "[2J")

                print(self.show_screen(point, current_direction))
        except ProgramFinished:
            print(self.show_screen(point, False))


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_grid()
        self.run_robot(input_data)
        return -1


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
