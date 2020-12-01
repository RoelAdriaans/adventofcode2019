from collections import defaultdict
from enum import IntEnum
from typing import List

from adventofcode2019.solutions.intcode import IntCode, ProgramFinished
from adventofcode2019.utils.abstract import FileReaderSolution
from adventofcode2019.utils.advent_utils import string_to_list_of_ints


class Tile(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

    @staticmethod
    def show(tile):
        if tile == Tile.EMPTY:
            return " "
        elif tile == Tile.WALL:
            return "░"
        elif tile == Tile.BLOCK:
            return "*"
        elif tile == Tile.PADDLE:
            return "▁"
        elif tile == Tile.BALL:
            return "O"


class Day13:
    screen: defaultdict
    score: int

    def show_screen(self):
        """
        Draw the screen on the console:
        - Empty : " "
        - Wall : "#"
        - Block : "*"
        - Paddle : "-"
        - Ball : "O"

        Size of the screen is:
        max x: 37
        max y: 19
        """
        max_y = max([point[1] for point in self.screen.keys()])
        max_x = max([point[0] for point in self.screen.keys()])
        grid = [f"Score: {self.score}"]
        for y in range(0, max_y + 1):
            row = []
            for x in range(0, max_x + 1):
                row.append(Tile.show(self.screen[x, y]))
            grid.append("".join(row))
        return "\n".join(grid)

    def draw_tile(self, x: int, y: int, tile: Tile) -> None:
        """ Draw a single tile """
        self.screen[(x, y)] = tile

    def get_location_for_tiles(self, type: Tile) -> List:
        tiles = [location for location, value in self.screen.items() if value == type]
        return tiles

    def run_arcade(self, input_data: str, free_to_play=False) -> int:
        self.screen = defaultdict(int)
        self.score = 0
        tile_obj = None

        instructions = string_to_list_of_ints(input_data)
        if free_to_play:
            # Is we allow free to play, Set instruction 0 to 2
            instructions[0] = 2

        intcode = IntCode()
        intcode.load_instructions(instructions)
        # Let's load the first instruction
        intcode.load_input_values([0])
        try:
            while True:
                x = intcode.run_return_or_raise()
                y = intcode.run_return_or_raise()
                tile = intcode.run_return_or_raise()
                if x == -1 and y == 0:
                    self.score = tile
                else:
                    tile_obj = Tile(tile)
                    self.draw_tile(x, y, tile_obj)
                if free_to_play and tile_obj == Tile.PADDLE:
                    pass
                    # Uncommit these lines to print the game progress
                    # from time import sleep
                    #
                    # sleep(0.01)
                    # print(chr(27) + "[2J")
                    # print(self.show_screen())

                # Compute there the ball is, and put the joystick to the right side
                ball = self.get_location_for_tiles(Tile.BALL)
                paddle = self.get_location_for_tiles(Tile.PADDLE)
                if ball and paddle:
                    # Check that we have the grid ready
                    if ball[0][0] < paddle[0][0]:
                        direction = -1
                    elif ball[0][0] > paddle[0][0]:
                        direction = 1
                    else:
                        direction = 0
                else:
                    direction = 0

                intcode.set_input_value([direction])

        except ProgramFinished:
            return self.score


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.run_arcade(input_data)

        block_tiles = self.get_location_for_tiles(Tile.BLOCK)
        return len(block_tiles)


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run_arcade(input_data, free_to_play=True)
