from utils.abstract import FileReaderSolution
from solutions.intcode import IntCode


class Day09:
    def run_computer(self, input_data: str, input_value: int) -> int:
        instructions = list(map(int, input_data.split(",")))
        intcode = IntCode()
        intcode.load_instructions(instructions)
        intcode.load_input_values([input_value])

        result = intcode.run_until_finished()
        return result[0]


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run_computer(input_data, 1)


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run_computer(input_data, 2)
