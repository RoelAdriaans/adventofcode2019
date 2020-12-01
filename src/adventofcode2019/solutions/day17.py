from collections import defaultdict
from typing import List, Tuple, Dict

from adventofcode2019.solutions.intcode import IntCode, ProgramFinished
from adventofcode2019.utils.abstract import FileReaderSolution
from adventofcode2019.utils.advent_utils import string_to_list_of_ints


class Day17:
    @staticmethod
    def print_grid(grid):
        for row in grid.values():
            print("".join([chr(i) for i in row.values()]), end="\n")

    def run_bot(self, input_data: str) -> Dict[int, Dict[int, int]]:
        instructions = string_to_list_of_ints(input_data)

        intcode = IntCode()
        intcode.load_instructions(instructions)
        chars = defaultdict(dict)
        try:
            row = 0
            col = 0
            while True:
                x = intcode.run_return_or_raise()
                if x == ord("\n"):
                    # Newline
                    row += 1
                    col = 0
                else:
                    chars[row][col] = x
                    col += 1
        except ProgramFinished:
            return chars

    @staticmethod
    def compute_points(grid_lines):
        """ Compute the points in the grid"""
        # First we will make a 2d array
        match = ord("#")
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
