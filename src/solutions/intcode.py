from typing import List
from collections import deque


class ProgramFinished(Exception):
    """
    This exception is raised when the program is finished.
    This exception is usually not a fatal error, but used for control structure.
    """

    pass


class IntCode:
    """
    This is the implementation for the Intcode computer, used in Advent of Code 2019.
    It is used in Day 2, 5 and more
    """

    program_counter = 0
    instructions: List[int]
    input_values: deque

    def __init__(self):
        self.reset()

    def reset(self):
        self.program_counter = 0
        self.instructions: List[int] = []
        self.input_values = deque([])

    def load_instructions(self, instructions: List[int]):
        self.program_counter = 0
        self.instructions = instructions[:]

    def load_input_values(self, input_values: List[int]):
        self.input_values.extend(input_values)

    def _parse_immediate_mode(self):
        current_opcode = self.instructions[self.program_counter]

        # Let's zeropad the string to make it easier to process
        str_opcode = f"{current_opcode:05}"
        # We are in Parameter modes
        current_opcode = int(str_opcode[-2:])
        param_1_position_mode = not bool(int(str_opcode[len(str_opcode) - 3]))
        param_2_position_mode = not bool(int(str_opcode[len(str_opcode) - 4]))

        return (
            current_opcode,
            param_1_position_mode,
            param_2_position_mode,
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

    def process_instruction(self):
        """ Process the current instruction and increate the program counter"""
        (
            current_opcode,
            param_1_position_mode,
            param_2_position_mode,
        ) = self._parse_immediate_mode()
        val_1 = self._get_value_from_location(param_1_position_mode, 1)
        val_2 = self._get_value_from_location(param_2_position_mode, 2)

        if current_opcode == 99:
            raise ProgramFinished

        if current_opcode == 1:
            # Add values
            store = self.instructions[self.program_counter + 3]
            value = val_1 + val_2
            self.instructions[store] = value
            self.program_counter += 4

        elif current_opcode == 2:
            # Multiply values
            store = self.instructions[self.program_counter + 3]
            value = val_1 * val_2
            self.instructions[store] = value
            self.program_counter += 4

        elif current_opcode == 3:
            # Use input
            store = self.instructions[self.program_counter + 1]
            value = self.input_values.popleft()
            self.instructions[store] = value
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

    def run(self) -> int:
        """
        Run the IntCode computer until the output is not 0 or None, or until
        the program runs out and raises an ProgramFinished exception.
        """
        res = 0
        try:
            while True:
                res = self.process_instruction()
                if res not in (0, None):
                    return res
        except ProgramFinished:
            return res

    def run_return_or_raise(self) -> int:
        while True:
            res = self.process_instruction()
            if res is not None:
                return res

    def run_multiple_output(self) -> List[int]:
        """
        Run the progam until a ProgramFinished error is raised, store all the outputs
        """
        results = []
        try:
            while True:
                res = self.process_instruction()
                if res is not None:
                    results.append(res)
        except ProgramFinished:
            return results

    def get_register(self, location: int) -> int:
        """
        Get the data that is in register `location`
        """
        return self.instructions[location]
