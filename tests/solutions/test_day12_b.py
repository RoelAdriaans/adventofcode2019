import pytest

from solutions.day12 import Day12PartB, Galaxy, Moon


class TestDay12PartB:
    def test_day12b(self):
        input_strings = [
            "<x=-1, y=0, z=2>",
            "<x=2, y=-10, z=-7>",
            "<x=4, y=-8, z=8>",
            "<x=3, y=5, z=-1>",
        ]
        input_string = "\n".join(input_strings)
        galaxy = Galaxy()
        galaxy.create_moons(input_string)

        compare_galaxy = Galaxy()
        compare_galaxy.create_moons(input_string)

        # Validate that the moons are the same in the begin
        assert compare_galaxy.moons == galaxy.moons

        galaxy.step()
        assert compare_galaxy.moons != galaxy.moons

        galaxy.step_multi(2771)
        assert compare_galaxy.moons == galaxy.moons

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                [
                    "<x=-1, y=0, z=2>",
                    "<x=2, y=-10, z=-7>",
                    "<x=4, y=-8, z=8>",
                    "<x=3, y=5, z=-1>",
                ],
                2772,
            ),
            (
                [
                    "<x=-8, y=-10, z=0>",
                    "<x=5, y=5, z=10>",
                    "<x=2, y=-7, z=3>",
                    "<x=9, y=-8, z=-3>",
                ],
                4686774924,
            ),
        ],
    )
    def test_day12b_solve(self, input_data, expected_result):
        input_string = "\n".join(input_data)
        solution = Day12PartB()
        result = solution.solve(input_string)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day12b_data(self):
        """ Result we got when we did the real solution """
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res == 0
