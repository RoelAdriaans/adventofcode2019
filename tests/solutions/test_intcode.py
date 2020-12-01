import pytest

from adventofcode2019.solutions.intcode import IntCode


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

    def test_load_save(self):
        intcode = IntCode()
        # Set relative base to 100,
        # Return value at location 1
        # Store input at 1
        intcode.load_input_values([42])
        intcode.load_instructions([9, 100, 4, 1, 3, 1, 4, 1])

        # Save computer
        save = intcode.save()

        output = intcode.run_return_or_raise()
        assert output == 100

        # Run the next instructions
        output = intcode.run_return_or_raise()
        assert output == 42

        # Load the computer again
        intcode.load(save)

        # Next output should be 100 again
        output = intcode.run_return_or_raise()
        assert output == 100
