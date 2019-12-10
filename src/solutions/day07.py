from utils.abstract import FileReaderSolution
from solutions.intcode import IntCode
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


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = list(map(int, input_data.split(",")))
        computer = IntCode()
        computer.load_instructions(instructions)


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
