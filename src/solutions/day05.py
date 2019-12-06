from utils.abstract import FileReaderSolution
from typing import List


class ProgramFinished(Exception):
    pass


class Day05:
    program_counter = 0
    instructions = []

    def load_instructions(self, instructions: List[int]):
        self.program_counter = 0
        self.instructions = instructions[:]

    def _parse_immediate_mode(self):
        current_opcode = self.instructions[self.program_counter]

        # Let's zeropad the string to make it easier to process
        str_opcode = f"{current_opcode:05}"
        # We are in Parameter modes
        current_opcode = int(str_opcode[-2:])
        param_1_position_mode = not bool(int(str_opcode[len(str_opcode) - 3]))
        param_2_position_mode = not bool(int(str_opcode[len(str_opcode) - 4]))
        param_3_position_mode = not bool(int(str_opcode[len(str_opcode) - 5]))

        return (
            current_opcode,
            param_1_position_mode,
            param_2_position_mode,
            param_3_position_mode,
        )

    def _get_value_from_location(self, position_mode: bool, position: int) -> int:
        """
        If `position_mode` is True, return the value in that position
        If `position_mode` is False,
        """
        try:
            value = self.instructions[self.program_counter + position]
        except IndexError:
            value = False
        if position_mode:
            try:
                return self.instructions[value]
            except IndexError:
                return False
        else:
            return value

    def process_instruction(self, input_value=None):
        """ Process the current instruction and increate the program counter"""
        current_opcode = self.instructions[self.program_counter]
        str_opcode = str(current_opcode)
        if len(str_opcode) >= 3:
            (
                current_opcode,
                param_1_position_mode,
                param_2_position_mode,
                param_3_position_mode,
            ) = self._parse_immediate_mode()
        else:
            # No long upcode, these will be false
            param_1_position_mode = True
            param_2_position_mode = True
            param_3_position_mode = True

        val_1 = self._get_value_from_location(param_1_position_mode, 1)
        val_2 = self._get_value_from_location(param_2_position_mode, 2)

        if current_opcode == 99:
            raise ProgramFinished

        if current_opcode == 1:
            # Add values
            store = self.instructions[self.program_counter + 3]
            self.instructions[store] = val_1 + val_2
            self.program_counter += 4

        elif current_opcode == 2:
            # Multiply values
            store = self.instructions[self.program_counter + 3]

            self.instructions[store] = val_1 * val_2
            self.program_counter += 4
        elif current_opcode == 3:
            # Use input
            store = self.instructions[self.program_counter + 1]
            self.instructions[store] = input_value
            self.program_counter += 2

        elif current_opcode == 4:
            # Return output
            output = self._get_value_from_location(param_1_position_mode, 1)

            self.program_counter += 2
            return output

        elif current_opcode == 5:
            # Jump-If-True: If the first parameter is *non-zero*, it sets the
            # instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            if val_1 != 0:
                self.program_counter = val_2
            else:
                self.program_counter += 3

        elif current_opcode == 6:
            # Jump-If-False: If the first parameter is *zero*, it sets the instruction
            # pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            if val_1 == 0:
                self.program_counter = val_2
            else:
                self.program_counter += 3

        elif current_opcode == 7:
            # less than: if the first parameter is less than the second parameter,
            # it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.
            store = self.instructions[self.program_counter + 3]

            if val_1 < val_2:
                self.instructions[store] = 1
            else:
                self.instructions[store] = 0
            self.program_counter += 4

        elif current_opcode == 8:
            # equals: if the first parameter is equal to the second parameter,
            # it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.
            store = self.instructions[self.program_counter + 3]

            if val_1 == val_2:
                self.instructions[store] = 1
            else:
                self.instructions[store] = 0
            self.program_counter += 4

        else:
            raise ValueError(f"Unknown opcode: {current_opcode}")

    def run(self, input_value):
        try:
            while True:
                res = self.process_instruction(input_value)
                if res not in (0, None):
                    return res
        except ProgramFinished:
            return res


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        # Technically not 100% correct, when res is non zero, if should check that the
        # next instructions terminates the program
        instructions = list(map(int, input_data.split(",")))
        self.load_instructions(instructions)
        res = False
        try:
            while True:
                res = self.process_instruction(1)
                if res not in (0, None):
                    return res
        except ProgramFinished:
            pass
        return res


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = list(map(int, input_data.split(",")))
        self.load_instructions(instructions)
        res = self.run(5)
        return res
