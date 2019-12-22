from typing import List, DefaultDict, Tuple
from collections import deque, defaultdict


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
    relative_base = 0
    instructions: DefaultDict[int, int]
    input_values: deque

    def __init__(self):
        self.reset()

    def reset(self):
        self.program_counter = 0
        self.relative_base = 0
        self.instructions = defaultdict(int)
        self.input_values = deque([])

    def load_instructions(self, instructions: List[int]):
        self.program_counter = 0
        for i, instruction in enumerate(instructions):
            self.instructions[i] = instruction

    def load_input_values(self, input_values: List[int]):
        self.input_values.extend(input_values)

    def _parse_immediate_mode(self) -> Tuple[int, int, int, int]:
        current_opcode = self.instructions[self.program_counter]
        opcode_length = len(str(current_opcode))
        if opcode_length >= 6:
            raise ValueError("Opcode 6 or longer!??!!?")
        # Let's zeropad the string to make it easier to process
        str_opcode = f"{current_opcode:05}"
        # We are in Parameter modes
        current_opcode = int(str_opcode[-2:])
        param_1_mode = int(str_opcode[len(str_opcode) - 3])
        param_2_mode = int(str_opcode[len(str_opcode) - 4])
        param_3_mode = int(str_opcode[len(str_opcode) - 5])

        return (
            current_opcode,
            param_1_mode,
            param_2_mode,
            param_3_mode,
        )

    def _get_value_from_location(self, position_mode: int, position: int) -> int:
        """
        If `position_mode` is True, return the value in that position
        If `position_mode` is False,
        """
        try:
            value = self.instructions[self.program_counter + position]
        except IndexError:
            value = False

        if position_mode == 0:
            try:
                return self.instructions[value]
            except IndexError:
                return False
        elif position_mode == 1:
            return value
        elif position_mode == 2:
            location = value + self.relative_base
            return self.instructions[location]
        else:
            raise ValueError(f"Not supported {position_mode=}")

    def _get_store_position(self, position_mode: int, position: int) -> int:
        """ position where we need to store the result of an output """

        if position_mode == 0:
            # Position Mode, this is the default mode.
            # Location is program_counter + offset
            return self.instructions[self.program_counter + position]
        elif position_mode == 1:
            # Advent of Code, day 5:
            # Parameters that an instruction writes to will never be in immediate mode.
            return False
        elif position_mode == 2:
            # Relative Mode
            value = self.instructions[self.program_counter + position]
            location = value + self.relative_base
            return location
        else:
            raise ValueError(f"Not supported {position_mode=}")

    def process_instruction(self):
        """ Process the current instruction and increate the program counter"""
        (
            current_opcode,
            param_1_mode,
            param_2_mode,
            param_3_mode,
        ) = self._parse_immediate_mode()
        val_1 = self._get_value_from_location(param_1_mode, 1)
        val_2 = self._get_value_from_location(param_2_mode, 2)

        # Store_x - where x is the number of operads for a function.
        # ag, multiply and store is multiple, two values and the 3th is store: store_3
        store_1 = self._get_store_position(param_1_mode, 1)
        store_3 = self._get_store_position(param_3_mode, 3)

        if current_opcode == 99:
            raise ProgramFinished

        if current_opcode == 1:
            # Add values
            value = val_1 + val_2
            self.instructions[store_3] = value
            self.program_counter += 4

        elif current_opcode == 2:
            # Multiply values
            value = val_1 * val_2
            self.instructions[store_3] = value
            self.program_counter += 4

        elif current_opcode == 3:
            # Use input
            value = self.input_values.popleft()
            self.instructions[store_1] = value
            self.program_counter += 2

        elif current_opcode == 4:
            # Return output
            self.program_counter += 2
            return val_1

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

            if val_1 < val_2:
                self.instructions[store_3] = 1
            else:
                self.instructions[store_3] = 0
            self.program_counter += 4

        elif current_opcode == 8:
            # equals: if the first parameter is equal to the second parameter,
            # it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.

            if val_1 == val_2:
                self.instructions[store_3] = 1
            else:
                self.instructions[store_3] = 0
            self.program_counter += 4

        elif current_opcode == 9:
            # Adjust the relative base.
            # adjusts the relative base by the value of its only parameter.
            # The relative base increases (or decreases, if the value is negative)
            # by the value of the parameter.
            self.relative_base += val_1
            self.program_counter += 2
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

    def run_until_finished(self) -> List[int]:
        result = []
        while True:
            try:
                res = self.run_return_or_raise()
                result.append(res)
            except ProgramFinished:
                return result

    def get_register(self, location: int) -> int:
        """
        Get the data that is in register `location`
        """
        return self.instructions[location]
