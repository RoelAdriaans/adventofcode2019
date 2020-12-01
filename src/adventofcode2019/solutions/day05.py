from adventofcode2019.solutions.intcode import IntCode
from adventofcode2019.utils.abstract import FileReaderSolution
from adventofcode2019.utils.advent_utils import string_to_list_of_ints


class Day05:
    pass


class Day05PartA(Day05, FileReaderSolution, IntCode):
    def solve(self, input_data: str) -> int:
        # Technically not 100% correct, when res is non zero, if should check that the
        # next instructions terminates the program
        instructions = string_to_list_of_ints(input_data)
        self.load_instructions(instructions)
        self.load_input_values([1])
        res = self.run()
        return res


class Day05PartB(Day05, FileReaderSolution, IntCode):
    def solve(self, input_data: str) -> int:
        instructions = string_to_list_of_ints(input_data)
        self.load_instructions(instructions)
        self.load_input_values([5])
        res = self.run()
        return res
