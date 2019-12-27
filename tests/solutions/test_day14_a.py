import pytest

from solutions.day14 import Day14PartA, Recipe, Chemical, NanoFactory


class TestDay14PartA:
    def test_recipy_reaction(self):
        input_recipe = "1 A, 2 B, 3 C => 2 D"
        recipe = Recipe.parse_recipe_string(input_recipe)
        assert len(recipe.inputs) == 3
        assert recipe.output.name == "D"
        assert recipe.output.consumable == 2

        assert recipe.inputs[0].name == "A"
        assert recipe.inputs[0].consumable == 1

    def test_reaction(self):
        test_data = [
            "10 ORE => 10 A",
            "1 ORE => 1 B",
            "7 A, 1 B => 1 C",
            "7 A, 1 C => 1 D",
            "7 A, 1 D => 1 E",
            "7 A, 1 E => 1 FUEL",
        ]
        input_lines = "\n".join(test_data)
        factory = NanoFactory()
        factory.read_input(input_lines)

        assert len(factory.recipes) == 6

        fuel = factory._get_requirement_for_one("FUEL", 1)
        assert fuel["A"] == 7
        assert fuel["E"] == 1

        # A is only created in mutiples of 10
        a = factory._get_requirement_for_one("A", 12)
        assert a["ORE"] == 20

        ore = factory.ore_needed_for_one_fuel()
        assert ore == 31

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                [
                    "10 ORE => 10 A",
                    "1 ORE => 1 B",
                    "7 A, 1 B => 1 C",
                    "7 A, 1 C => 1 D",
                    "7 A, 1 D => 1 E",
                    "7 A, 1 E => 1 FUEL",
                ],
                31,
            )
        ],
    )
    def test_day14a_solve(self, input_data, expected_result):
        input_lines = "\n".join(input_data)
        solution = Day14PartA()
        result = solution.solve(input_lines)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day14a_data(self):
        """ Result we got when we did the real solution """
        solution = Day14PartA()
        res = solution("day_14/day14.txt")
        assert res == 0
