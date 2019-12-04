from utils.abstract import FileReaderSolution
import re


class Day04:
    @staticmethod
    def is_valid_length(number_str: str) -> bool:
        """Is this string exactly 6 characters"""
        # Technically, the string will always be 6 long, we define that input.
        # Keeping the test anyway, it makes this rule more implicit.

        return len(number_str) == 6

    @staticmethod
    def is_consecutive(number_str: str) -> bool:
        for digit in range(0, 10):
            str_digit = str(digit)
            replaced = number_str.replace(f"{str_digit}{str_digit}", "")
            if len(replaced) <= 5:
                return True
        return False

    @staticmethod
    def is_going_up(number_str: str) -> bool:
        # Validate that the numbers go up or are the same.
        max_found = float("-inf")

        for digit in number_str:
            if int(digit) >= max_found:
                max_found = int(digit)
            else:
                return False
        return True

    @staticmethod
    def is_valid_part_a(int_input: int) -> bool:
        str_input = str(int_input)
        if all(
            [
                Day04.is_valid_length(str_input),
                Day04.is_consecutive(str_input),
                Day04.is_going_up(str_input),
            ]
        ):
            return True

        return False

    @staticmethod
    def is_valid_part_b(int_input: int) -> bool:
        str_input = str(int_input)
        if len(str_input) != 6:
            return False

        two_consecetive = False
        digit_in = False

        for digit in range(0, 10):
            str_digit = str(digit)
            replaced = str_input.replace(f"{str_digit}{str_digit}", "")
            if len(replaced) == 4:
                two_consecetive = True
            if str_digit in replaced:
                # Still a digit in there
                digit_in = True

        if not two_consecetive:
            return False

        if digit_in:
            return False

        max_found = float("-inf")

        for digit in str_input:
            if int(digit) >= max_found:
                max_found = int(digit)
            else:
                return False

        return True


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lower, uper = input_data.split("-")
        lower = int(lower)
        uper = int(uper)
        counter = 0
        for x in range(lower, uper + 1):
            valid = self.is_valid_part_a(x)
            if valid:
                counter += 1
        return counter


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:

        lower, uper = input_data.split("-")
        lower = int(lower)
        uper = int(uper)
        counter = 0
        for x in range(lower, uper + 1):
            valid = self.is_valid_part_b(x)
            if valid:
                counter += 1
        return counter
