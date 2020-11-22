from typing import List, Tuple

from solutions.intcode import IntCode, ProgramFinished
from utils.abstract import FileReaderSolution
from utils.advent_utils import string_to_list_of_ints


class Day17:
    @staticmethod
    def print_grid(grid):
        for x in grid:
            print(chr(x), end="")

    def run_bot(self, input_data: str) -> List[int]:
        instructions = string_to_list_of_ints(input_data)

        intcode = IntCode()
        intcode.load_instructions(instructions)
        chars = []
        try:
            while True:
                x = intcode.run_return_or_raise()
                chars.append(x)
        except ProgramFinished:
            return chars

    @staticmethod
    def grid_to_lists(grid: List[int]) -> List[List]:
        """ Convert to a 2d grid"""
        width = grid.index(ord("\n")) + 1
        num_loops = len(grid) / width
        res = []
        for i in range(int(num_loops)):
            idx_start = i * width
            idx_end = (i * width) + width - 1
            res.append(grid[idx_start:idx_end])
        return res

    @staticmethod
    def compute_points(grid):
        """ Compute the points in the grid"""
        # First we will make a 2d array
        match = ord("#")
        grid_lines = Day17.grid_to_lists(grid)
        matches = []

        for x in range(1, len(grid_lines) - 1):
            for y in range(1, len(grid_lines[0]) - 1):
                left = grid_lines[x - 1][y]
                right = grid_lines[x + 1][y]
                top = grid_lines[x][y - 1]
                bottom = grid_lines[x][y + 1]
                current = grid_lines[x][y]

                if (
                    left == match
                    and right == match
                    and top == match
                    and bottom == match
                    and current == match
                ):
                    matches.append((x, y))
                    grid_lines[x][y] = "O"

        return matches

    @staticmethod
    def compute_scores(matches: List[Tuple[int, int]]) -> int:
        return sum([x[0] * x[1] for x in matches])


class Day17PartA(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        grid = self.run_bot(input_data)
        markers = self.compute_points(grid)
        score = self.compute_scores(matches=markers)

        return score


class Day17PartB(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
