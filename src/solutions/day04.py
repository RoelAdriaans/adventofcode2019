from utils.abstract import FileReaderSolution


class Day04:
    @staticmethod
    def is_valid(int_input: int) -> bool:
        str_input = str(int_input)
        if len(str_input) != 6:
            return False

        two_consecetive = False
        for digit in range(0, 10):
            str_digit = str(digit)
            replaced = str_input.replace(f"{str_digit}{str_digit}", "")
            if len(replaced) <= 5:
                two_consecetive = True
                break

        if not two_consecetive:
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
        for x in range(lower, uper+1):
            valid = self.is_valid(x)
            if valid:
                counter += 1
        return counter


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
