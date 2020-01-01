from collections import defaultdict
from enum import IntEnum
from typing import List, Tuple, Union
from time import sleep

from solutions.intcode import IntCode, ProgramFinished
from utils.abstract import FileReaderSolution
from utils.advent_utils import string_to_list_of_ints


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
            turn_dict = {
                1: 4,
                2: 3,
                3: 1,
                4: 2
            }
        else:
            turn_dict = {
                1: 3,
                2: 4,
                3: 2,
                4: 1
            }

        new_direction = turn_dict[current_direction.value]
        return Movement(new_direction)

    @staticmethod
    def direction_update_x_y(
        current_direction: "Movement", x: int, y: int
    ) -> Tuple[int, int]:
        """
        Update the coordinate if the movement succeeded

        :param current_direction: The current direction we're moving in
        :param x: Current position
        :param y: Current position
        :return: Tuple (x, y) with new direction
        """
        if current_direction == Movement.NORTH:
            return x, y + 1
        elif current_direction == Movement.SOUTH:
            return x, y - 1
        elif current_direction == Movement.EAST:
            return x + 1, y
        elif current_direction == Movement.WEST:
            return x - 1, y
        else:
            raise ValueError(f"Invalid current direction {current_direction}")


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


class Day15:
    grid: defaultdict

    def show_screen(self, droid_x: int, droid_y: int, direction: Union[bool, Movement]):
        """
        Draw the current grid on the console:
        """
        max_y = max([point[1] for point in self.grid.keys()])
        max_x = max([point[0] for point in self.grid.keys()])
        min_y = min([point[1] for point in self.grid.keys()])
        min_x = min([point[0] for point in self.grid.keys()])
        output = []
        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):
                if y == droid_y and x == droid_x:
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
                    if (x, y) in self.grid:
                        row.append(Tile.show(self.grid[x, y]))
                    else:
                        row.append(" ")
            output.append("".join(row))
        return "\n".join(output)

    def run_robot(self, input_data: str):
        self.grid = defaultdict(int)
        instructions = string_to_list_of_ints(input_data)
        intcode = IntCode()
        current_direction = Movement.NORTH

        def return_input():
            # Implement Dijkstra's thing here. Or, only when we have the grid
            print(f"Returning input: {current_direction} ({current_direction.value})")
            return current_direction.value

        intcode.set_input_function(return_input)
        intcode.load_instructions(instructions)
        # Current location of the bot:
        x, y = 0, 0

        # First, Let's see if we can build anything
        try:
            while True:
                result = intcode.run_return_or_raise()
                status = StatusCode(result)
                if status == StatusCode.HIT_WALL:
                    # The position we tried to move into was a wall:
                    wall_x, wall_y = Movement.direction_update_x_y(
                        current_direction, x, y
                    )
                    self.grid[wall_x, wall_y] = Tile.WALL
                    current_direction = Movement.rotate(current_direction, 1)

                elif status == StatusCode.MOVE_REQUESTED:
                    x, y = Movement.direction_update_x_y(current_direction, x, y)
                    self.grid[x, y] = Tile.OPEN

                elif status == StatusCode.MOVE_REQUESTED_INSIDE:
                    self.grid[x, y] = Tile.OXYGEN


                sleep(0.1)
                print(chr(27) + "[2J")

                print(self.show_screen(x, y, current_direction))
        except ProgramFinished:
            print(self.show_screen(x, y, False))


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.run_robot(input_data)
        return -1


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
