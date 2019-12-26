from utils.abstract import FileReaderSolution
from solutions.intcode import IntCode, ProgramFinished
from utils.advent_utils import string_to_list_of_ints
from enum import IntEnum
from collections import defaultdict

class Tile(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class Day13:
    screen: defaultdict

    def draw_tile(self, x: int, y: int, tile: Tile) -> None:
        """ Draw a single tile """
        self.screen[(x, y)] = tile

    def run_arcade(self, input_data: str) -> int:
        self.screen = defaultdict(int)

        instructions = string_to_list_of_ints(input_data)

        intcode = IntCode()
        intcode.load_instructions(instructions)
        try:
            while True:
                x = intcode.run_return_or_raise()
                y = intcode.run_return_or_raise()
                tile = intcode.run_return_or_raise()
                tile_obj = Tile(tile)
                self.draw_tile(x, y, tile_obj)

        except ProgramFinished:
            return 0


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.run_arcade(input_data)

        block_tiles = [
            location for location, value in self.screen.items() if value == Tile.BLOCK
        ]
        return len(block_tiles)


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
