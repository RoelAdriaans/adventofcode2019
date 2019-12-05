from utils.abstract import FileReaderSolution
from typing import List


class Day05:
    program_counter = 0
    instructions = []

    def load_instructions(self, instructions: List[int]):
        self.program_counter = 0
        self.instructions = instructions[:]

    def _get_location(self):
        current_opcode = self.instructions[self.program_counter]
        str_opcode = str(current_opcode)

        if len(str_opcode) >= 4:
            # We are in Parameter modes
            current_opcode = int(str_opcode[-2:])
            param_1_position_mode = bool(str_opcode[len(str_opcode) - 3])
            param_2_position_mode = bool(str_opcode[len(str_opcode) - 4])
            if len(str_opcode) == 5:
                param_3_position_mode = bool(str_opcode[len(str_opcode) - 5])
            else:
                param_3_position_mode = None
                param_is


    def process_instruction(self):
        """ Process the current instruction and increate the program counter"""
        current_opcode = self.instructions[self.program_counter]
        str_opcode = str(current_opcode)

        if current_opcode == 99:
            return

        if current_opcode == 1:
            pos_1 = self.instructions[self.program_counter + 1]
            pos_2 = self.instructions[self.program_counter + 2]
            store = self.instructions[self.program_counter + 3]

            add = self.instructions[pos_1] + self.instructions[pos_2]
            self.instructions[store] = add
            self.program_counter += 4

        elif current_opcode == 2:
            pos_1 = self.instructions[self.program_counter + 1]
            pos_2 = self.instructions[self.program_counter + 2]
            store = self.instructions[self.program_counter + 3]

            mult = self.instructions[pos_1] * self.instructions[pos_2]
            self.instructions[store] = mult
            self.program_counter += 4
        elif current_opcode == 3:
            input_value = 1
            store = self.instructions[self.program_counter + 1]

            self.instructions[store] = input_value

        elif current_opcode == 4:
            output = self.instructions[self.program_counter + 1]
            self.program_counter += 2
            print(output)
        else:
            raise ValueError("Unknown opcode")


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
