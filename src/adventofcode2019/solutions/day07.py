import itertools
from typing import List, Tuple

from adventofcode2019.solutions.intcode import IntCode, ProgramFinished
from adventofcode2019.utils.abstract import FileReaderSolution
from adventofcode2019.utils.advent_utils import string_to_list_of_ints


class Day07:
    @staticmethod
    def compute_results_for_looped_sequence(
        instructions: List[int], sequence: Tuple
    ) -> int:
        """
        For program `instructions`, compute the result for the sequence in the string
        `sequence`, eg "01234"
        """
        amplifiers = []
        # First we create the 5 amplifiers
        for amplifier_number in sequence:
            amplifier = IntCode()
            amplifier.load_instructions(instructions)
            amplifier.load_input_values([amplifier_number])
            amplifiers.append(amplifier)

        # And now, run
        last_value = 0
        num_done = 0
        result = 0
        while True:
            for amplifier in amplifiers:
                amplifier.load_input_values([result])
                try:
                    result = amplifier.run_return_or_raise()

                except ProgramFinished:
                    # This computer is done!
                    num_done += 1
                    if num_done == 5:
                        return last_value
                else:
                    last_value = result

    def get_best_looped_sequence(
        self, start, stop, instructions: List[int]
    ) -> Tuple[str, int]:
        """ Get the sequence with the best output """
        # Generate all the options
        # We loop because we have 10 computers,
        max_result = -1
        max_sequence: Tuple[int, ...] = (0, 0, 0, 0, 0)
        for sequence in itertools.permutations(range(start, stop)):
            result = self.compute_results_for_looped_sequence(instructions, sequence)
            if result > max_result:
                max_sequence = sequence
                max_result = result
        return "".join(map(str, max_sequence)), max_result


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = string_to_list_of_ints(input_data)
        sequence, thrust = self.get_best_looped_sequence(0, 5, instructions)
        return thrust


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = string_to_list_of_ints(input_data)
        sequence, thrust = self.get_best_looped_sequence(5, 10, instructions)
        return thrust
