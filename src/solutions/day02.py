from utils.abstract import FileReaderSolution
from typing import List


class Day02:
    program_counter = 0

    def look_at_opcodes(self, opcodes: List[int]) -> List[int]:
        self.program_counter = 0
        while True:
            current_opcode = opcodes[self.program_counter]
            if current_opcode == 99:
                return opcodes

            pos_1 = opcodes[self.program_counter + 1]
            pos_2 = opcodes[self.program_counter + 2]
            store = opcodes[self.program_counter + 3]

            if current_opcode == 1:
                add = opcodes[pos_1] + opcodes[pos_2]
                opcodes[store] = add
                self.program_counter += 4

            elif current_opcode == 2:
                mult = opcodes[pos_1] * opcodes[pos_2]
                opcodes[store] = mult
                self.program_counter += 4
            else:
                raise ValueError("Unknown opcode")


class Day02PartA(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        opcodes = [int(digit) for digit in input_data.split(",")]
        opcodes[1] = 12
        opcodes[2] = 2
        result = self.look_at_opcodes(opcodes=opcodes)
        return result[0]


class Day02PartB(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        for noun in range(100):
            for verb in range(100):
                opcodes = [int(digit) for digit in input_data.split(",")]
                opcodes[1] = noun
                opcodes[2] = verb
                result = self.look_at_opcodes(opcodes=opcodes)
                if result[0] == 19690720:
                    return 100 * noun + verb
        raise ValueError("Result not found")
