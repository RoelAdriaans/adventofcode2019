from adventofcode2019.solutions.day09 import Day09PartA
from adventofcode2019.solutions.intcode import IntCode


class TestDay09PartA:
    def test_day09a_replicating_opcode(self):
        """ takes no input and produces a copy of itself as output."""
        instructions = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
        opcodes = [int(digit) for digit in instructions.split(",")]
        intcode = IntCode()
        intcode.load_instructions(opcodes)
        result = intcode.run_until_finished()
        assert result == opcodes

    def test_day09a_16_digits(self):
        """ should output a 16-digit number."""
        instructions = "1102,34915192,34915192,7,4,7,99,0"
        opcodes = [int(digit) for digit in instructions.split(",")]
        intcode = IntCode()
        intcode.load_instructions(opcodes)
        result = intcode.run()
        assert len(str(result)) == 16

    def test_day09a_output_large_number(self):
        """  should output the large number in the middle. """
        instructions = "104,1125899906842624,99"
        opcodes = [int(digit) for digit in instructions.split(",")]
        intcode = IntCode()
        intcode.load_instructions(opcodes)
        result = intcode.run()
        assert result == opcodes[1]

    def test_day09a_data(self):
        """ Result we got when we did the real solution """
        solution = Day09PartA()
        res = solution("day_09/day09.txt")
        assert res != 203
        assert res == 3380552333
