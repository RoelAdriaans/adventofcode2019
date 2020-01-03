from collections import deque
from enum import IntEnum
from typing import Dict, NamedTuple, Optional

from solutions.intcode import IntCode
from utils.abstract import FileReaderSolution
from utils.advent_utils import string_to_list_of_ints


class Point(NamedTuple):
    x: int
    y: int


class Direction(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    @staticmethod
    def direction_update_x_y(current_direction: "Direction", point: Point) -> Point:
        """
        Update the coordinate if the movement succeeded

        :param current_direction: The current direction we're moving in
        :param point: Current position
        :return: Point) with new direction
        """
        if current_direction == Direction.NORTH:
            return Point(point.x, point.y - 1)
        elif current_direction == Direction.SOUTH:
            return Point(point.x, point.y + 1)
        elif current_direction == Direction.EAST:
            return Point(point.x + 1, point.y)
        elif current_direction == Direction.WEST:
            return Point(point.x - 1, point.y)
        else:
            raise ValueError(f"Invalid current direction {current_direction}")


class StatusCode(IntEnum):
    HIT_WALL = 0
    MOVE_REQUESTED = 1
    OXYGEN = 2


class Tile(IntEnum):
    DROID = 0
    WALL = 1
    OPEN = 2
    OXYGEN = 3

    @staticmethod
    def show(tile):
        values = {
            Tile.DROID: "D",
            Tile.WALL: "░",
            Tile.OPEN: " ",
            Tile.OXYGEN: "*",
        }
        return values[tile]


class Location:
    """ Location / Pixel in the maze """

    point: Point
    location_type: Optional[Tile]

    def __init__(self, point: Point, location_type: Optional[Tile] = None):
        self.point = point
        self.location_type = location_type

    def __repr__(self):
        tile = Tile.show(self.location_type)
        return f"({self.point} - {tile}"


class VisitQueue(NamedTuple):
    computer_state: str
    # direction: Union[bool, Direction]
    point: Point
    num_steps: int


class Day15:
    grid: Dict[Point, Location]
    oxygen_points: set

    def show_screen(self, droid_point: Point):
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
                    row.append("D")
                else:
                    if point in self.grid:
                        row.append(Tile.show(self.grid[point].location_type))
                    else:
                        row.append(" ")
            output.append("".join(row))
        return "\n".join(output)

    def run_robot(self, input_data: str):
        self.grid = {}
        self.oxygen_points = set()

        visited = {Point(0, 0)}

        input_direction = 0

        def get_input() -> int:
            return input_direction

        # computer = IntcodeComputer(PROGRAM, get_input)
        computer = IntCode()
        instructions = string_to_list_of_ints(input_data)
        computer.load_instructions(instructions)
        computer.set_input_function(get_input)

        # frontier will be a deque with VisitQueue
        frontier = deque(
            [
                VisitQueue(
                    computer_state=computer.save(), point=Point(0, 0), num_steps=0,
                )
            ]
        )

        while frontier:
            queue = frontier.popleft()

            for direction in Direction:
                computer.load(queue.computer_state)
                input_direction = direction.value
                status = StatusCode(computer.run_return_or_raise())
                if status == StatusCode.OXYGEN:
                    self.grid[queue.point] = Location(
                        point=queue.point, location_type=Tile.OXYGEN
                    )

                    self.oxygen_points.add(
                        (self.grid[queue.point], queue.num_steps + 1)
                    )
                elif status == StatusCode.HIT_WALL:
                    new_loc = Direction.direction_update_x_y(
                        current_direction=direction, point=queue.point
                    )
                    self.grid[new_loc] = Location(
                        point=new_loc, location_type=Tile.WALL
                    )

                elif status == StatusCode.MOVE_REQUESTED:
                    new_loc = Direction.direction_update_x_y(
                        current_direction=direction, point=queue.point
                    )
                    if new_loc not in visited:
                        # We only add a location if we haven't been there before
                        visited.add(new_loc)
                        frontier.append(
                            VisitQueue(
                                computer_state=computer.save(),
                                point=new_loc,
                                num_steps=queue.num_steps + 1,
                            )
                        )
                        self.grid[queue.point] = Location(
                            point=queue.point, location_type=Tile.OPEN
                        )


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.run_robot(input_data)
        oxygen = self.oxygen_points.pop()
        return oxygen[1]


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
