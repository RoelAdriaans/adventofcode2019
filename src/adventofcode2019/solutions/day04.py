from adventofcode2019.utils.abstract import FileReaderSolution
from adventofcode2019.utils.advent_utils import string_to_list_of_ints


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
    def is_consecutive_no_larger_group(number_str: str) -> bool:
        """ Check for values, if there is any there is any double digit, success """
        for x in str(number_str):
            if str(number_str).count(x) == 2:
                return True
        return False

    @staticmethod
    def is_going_up(number_str: str) -> bool:
        # Validate that the numbers go up or are the same.
        sorted_str = "".join(sorted(number_str))
        return sorted_str == number_str

    @staticmethod
    def is_valid_part_a(int_input: int) -> bool:
        str_input = str(int_input)
        return all(
            [
                Day04.is_valid_length(str_input),
                Day04.is_consecutive(str_input),
                Day04.is_going_up(str_input),
            ]
        )

    @staticmethod
    def is_valid_part_b(int_input: int) -> bool:
        str_input = str(int_input)
        return all(
            [
                Day04.is_valid_length(str_input),
                Day04.is_consecutive_no_larger_group(str_input),
                Day04.is_going_up(str_input),
            ]
        )


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lower, upper = string_to_list_of_ints(input_data, "-")
        counter = sum(self.is_valid_part_a(x) for x in range(lower, upper + 1))
        return counter


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lower, upper = string_to_list_of_ints(input_data, "-")
        counter = sum(self.is_valid_part_b(x) for x in range(lower, upper + 1))
        return counter
