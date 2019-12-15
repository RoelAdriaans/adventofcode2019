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
