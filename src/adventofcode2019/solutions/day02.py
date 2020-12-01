from adventofcode2019.solutions.intcode import IntCode
from adventofcode2019.utils.abstract import FileReaderSolution


class Day02:
    pass


class Day02PartA(Day02, FileReaderSolution, IntCode):
    def solve(self, input_data: str) -> int:
        opcodes = [int(digit) for digit in input_data.split(",")]
        opcodes[1] = 12
        opcodes[2] = 2
        self.load_instructions(opcodes)
        self.run()
        return self.get_register(0)


class Day02PartB(Day02, FileReaderSolution, IntCode):
    def solve(self, input_data: str) -> int:
        opcodes = [int(digit) for digit in input_data.split(",")]

        for noun in range(100):
            for verb in range(100):
                instructions = opcodes[:]
                instructions[1] = noun
                instructions[2] = verb
                self.load_instructions(instructions)
                self.run()
                result = self.get_register(0)
                if result == 19690720:
                    return 100 * noun + verb
        raise ValueError("Result not found")
