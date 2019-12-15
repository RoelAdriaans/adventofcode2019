from utils.abstract import FileReaderSolution
from solutions.intcode import IntCode, ProgramFinished
from typing import List, Tuple, Union
import itertools


class Day07:
    def compute_results_for_sequence(
        self, instructions: List[int], sequence: Tuple
    ) -> int:
        """
        For program `instructions`, compute the result for the sequence in the string
        `sequence`, eg "01234"
        """
        results = [0]
        for amplifier in sequence:
            intcode = IntCode()

            intcode.load_instructions(instructions)
            intcode.load_input_values([amplifier])
            intcode.load_input_values(results)
            results = intcode.run_multiple_output()
        return results[0]

    def get_best_sequence(
        self, instructions: List[int]
    ) -> Tuple[str, Union[float, int]]:
        """ Get the sequence with the best output"""
        # Generate all the options
        # (eg, 1 -> 01 and 10, 2: 012 021 102 ...)
        max_result = float("-inf")
        max_sequence = ""
        for sequence in itertools.permutations(range(5)):

            result = self.compute_results_for_sequence(instructions, sequence)
            if result > max_result:
                max_sequence = sequence
                max_result = result
        return "".join(map(str, max_sequence)), max_result

    def compute_results_for_looped_sequence(
        self, instructions: List[int], sequence: Tuple
    ) -> int:
        """
        For program `instructions`, compute the result for the sequence in the string
        `sequence`, eg "01234"
        """
        amplifiers = []
        # First we create the 5 amplifiers
        for amplifier_number in sequence:
            amplifier = IntCode()
            amplifier.done = False
            amplifier.load_instructions(instructions)
            amplifier.load_input_values([amplifier_number])
            amplifiers.append(amplifier)

        # And now, run
        last_value = None
        num_done = 0
        # Run the sequence:
        result = 0
        while True:
            for amplifier in amplifiers:
                if amplifier.done:
                    continue
                amplifier.load_input_values([result])
                try:
                    result = amplifier.run_return_or_raise()

                except ProgramFinished:
                    # Program is done!
                    amplifier.done = True
                    num_done += 1
                    if num_done == 5:
                        return last_value
                else:
                    last_value = result

            # We have done a loop, let's check if this is the bigest value
            if result is None:
                return last_value
            else:
                last_value = result

    def get_best_looped_sequence(
        self, instructions: List[int]
    ) -> Tuple[str, Union[float, int]]:
        """ Get the sequence with the best outpu t"""
        # Generate all the options
        # We loop because we have 10 computers,
        max_result = float("-inf")
        max_sequence = ""
        for sequence in itertools.permutations(range(5, 10)):
            result = self.compute_results_for_looped_sequence(instructions, sequence)
            if result > max_result:
                max_sequence = sequence
                max_result = result
        return "".join(map(str, max_sequence)), max_result


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = list(map(int, input_data.split(",")))
        sequence, thrust = self.get_best_sequence(instructions)
        return thrust


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = list(map(int, input_data.split(",")))
        sequence, thrust = self.get_best_looped_sequence(instructions)
        return thrust
