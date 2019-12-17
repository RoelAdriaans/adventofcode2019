import pytest

from solutions.intcode import IntCode


class TestIntcode:
    def test_intcode_unknown_opcode(self):
        intcode = IntCode()
        instruction = [55, 44, 33, 22]
        intcode.load_instructions(instruction)
        with pytest.raises(ValueError) as excinfo:
            intcode.run()

        assert "Unknown opcode: 55" in str(excinfo.value)

    def test_relative_base(self):
        intcode = IntCode()
        intcode.relative_base = 2000
        intcode.load_instructions([109, 19, 204, -34])
        intcode.instructions[1985] = 1982
        intcode.process_instruction()

        assert intcode.relative_base == 2019

        result = intcode.process_instruction()
        assert result == 1982
