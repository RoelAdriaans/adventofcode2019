import json
from collections import defaultdict, deque
from enum import IntEnum
from typing import DefaultDict, List, Tuple


class ProgramFinished(Exception):
    """
    This exception is raised when the program is finished.
    This exception is usually not a fatal error, but used for control structure.
    """

    pass


class OperatingMode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Opcode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    STORE_INPUT = 3
    RETURN_OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_RELATIVE_BASE = 9

    END_PROGRAM = 99


class IntCode:
    """
    This is the implementation for the Intcode computer, used in Advent of Code 2019.
    It is used in Day 2, 5 and more
    """

    program_counter = 0
    relative_base = 0
    instructions: DefaultDict[int, int]
    input_values: deque
    input_function = None

    def __init__(self):
        self.reset()

    def load(self, load_data: str):
        """Load the computer from a json string.
        This method only restores the state, not the input values or function.
        """
        data = json.loads(load_data)
        self.program_counter = data["program_counter"]
        self.relative_base = data["relative_base"]

        # Load the instructions into a defaultDict
        self.instructions = defaultdict(int)
        for location, value in data["instructions"].items():
            self.instructions[int(location)] = int(value)

    def save(self) -> str:
        """ Save the state as a json string """
        data = {
            "program_counter": self.program_counter,
            "relative_base": self.relative_base,
            "instructions": self.instructions.copy(),
        }
        return json.dumps(data)

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

    def set_input_value(self, input_values: List[int]):
        self.input_values = deque(input_values)

    def set_input_function(self, input_function):
        self.input_function = input_function

    def _parse_current_opcode(self) -> Tuple[int, List[int]]:
        current_opcode = self.instructions[self.program_counter]
        opcode_length = len(str(current_opcode))
        if opcode_length >= 6:
            raise ValueError("Opcode 6 or longer!??!!?")
        # Let's zeropad the string to make it easier to process
        str_opcode = f"{current_opcode:05}"
        # We are in Parameter modes
        current_opcode = int(str_opcode[-2:])
        modes = [int(str_opcode[len(str_opcode) - place]) for place in (3, 4, 5)]

        return current_opcode, modes

    def _get_value_from_location(self, position_mode: int, position: int) -> int:
        """
        If `position_mode` is 0, use Use position mode,
        Return value at the location defined by program counter + position.

        If `position_mode` is 1, use immediate mode.
        Return the value at program counter + position.

        If `position_mode` is 2, use relative posision mode.
        Return value at the location defined by program counter + position +
        relative base.
        """
        try:
            value = self.instructions[self.program_counter + position]
        except IndexError:
            value = False

        if position_mode == OperatingMode.POSITION:
            try:
                return self.instructions[value]
            except IndexError:
                return False
        elif position_mode == OperatingMode.IMMEDIATE:
            return value
        elif position_mode == OperatingMode.RELATIVE:
            location = value + self.relative_base
            return self.instructions[location]
        else:
            raise ValueError(f"Not supported {position_mode=}")

    def _get_store_position(self, position_mode: int, position: int) -> int:
        """
        Return the position in memory where we need to store a value.
        This function does not store the value itselve!

        If `position_mode` is 0, use Use position mode,
        Return location defined at the location by program counter + position.

        If `position_mode` is 1, Return False. Not used according to Day 5.

        If `position_mode` is 0, use Use relative position mode,
        Return location defined at the location by program counter + position, and add
        the relative base location.
        """

        if position_mode == OperatingMode.POSITION:
            # Position Mode, this is the default mode.
            # Location is program_counter + offset
            return self.instructions[self.program_counter + position]
        elif position_mode == OperatingMode.IMMEDIATE:
            # Advent of Code, day 5:
            # Parameters that an instruction writes to will never be in immediate mode.
            return False
        elif position_mode == OperatingMode.RELATIVE:
            # Relative Mode
            value = self.instructions[self.program_counter + position]
            location = value + self.relative_base
            return location
        else:
            raise ValueError(f"Not supported {position_mode=}")

    def process_instruction(self):
        """ Process the current instruction and increase the program counter"""
        (current_opcode, position_modes) = self._parse_current_opcode()
        val_1 = self._get_value_from_location(position_modes[0], 1)
        val_2 = self._get_value_from_location(position_modes[1], 2)

        # Store_x - where x is the number of operads for a function.
        # ag, multiply and store is multiple, two values and the 3th is store: store_3
        store_1 = self._get_store_position(position_modes[0], 1)
        store_3 = self._get_store_position(position_modes[2], 3)

        if current_opcode == Opcode.END_PROGRAM:
            raise ProgramFinished

        if current_opcode == Opcode.ADD:
            value = val_1 + val_2
            self.instructions[store_3] = value
            self.program_counter += 4

        elif current_opcode == Opcode.MULTIPLY:
            value = val_1 * val_2
            self.instructions[store_3] = value
            self.program_counter += 4

        elif current_opcode == Opcode.STORE_INPUT:
            if self.input_function:
                value = self.input_function()
            else:
                value = self.input_values.popleft()
            self.instructions[store_1] = value
            self.program_counter += 2

        elif current_opcode == Opcode.RETURN_OUTPUT:
            self.program_counter += 2
            return val_1

        elif current_opcode == Opcode.JUMP_IF_TRUE:
            # If the first parameter is *non-zero*, it sets the
            # instruction pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            if val_1 != 0:
                self.program_counter = val_2
            else:
                self.program_counter += 3

        elif current_opcode == Opcode.JUMP_IF_FALSE:
            # If the first parameter is *zero*, it sets the instruction
            # pointer to the value from the second parameter.
            # Otherwise, it does nothing.
            if val_1 == 0:
                self.program_counter = val_2
            else:
                self.program_counter += 3

        elif current_opcode == Opcode.LESS_THAN:
            # If the first parameter is less than the second parameter,
            # it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.

            if val_1 < val_2:
                self.instructions[store_3] = 1
            else:
                self.instructions[store_3] = 0
            self.program_counter += 4

        elif current_opcode == Opcode.EQUALS:
            # If the first parameter is equal to the second parameter,
            # it stores 1 in the position given by the third parameter.
            # Otherwise, it stores 0.

            if val_1 == val_2:
                self.instructions[store_3] = 1
            else:
                self.instructions[store_3] = 0
            self.program_counter += 4

        elif current_opcode == Opcode.ADJUST_RELATIVE_BASE:
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
