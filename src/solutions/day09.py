from utils.abstract import FileReaderSolution
from solutions.intcode import IntCode


class Day09:
    pass


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = list(map(int, input_data.split(",")))
        intcode = IntCode()
        intcode.load_instructions(instructions)
        intcode.load_input_values([1])

        result = intcode.run_until_finished()
        return result[0]


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return 0
