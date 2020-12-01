import pytest

from adventofcode2019.solutions.day14 import Day14PartA, NanoFactory, Recipe


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

        ore = factory.ore_needed_for_n_fuel(1)
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
            ),
            (
                [
                    "9 ORE => 2 A",
                    "8 ORE => 3 B",
                    "7 ORE => 5 C",
                    "3 A, 4 B => 1 AB",
                    "5 B, 7 C => 1 BC",
                    "4 C, 1 A => 1 CA",
                    "2 AB, 3 BC, 4 CA => 1 FUEL",
                ],
                165,
            ),
            (
                [
                    "171 ORE => 8 CNZTR",
                    "7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => "
                    "4 PLWSL",
                    "114 ORE => 4 BHXH",
                    "14 VRPVC => 6 BMBT",
                    "6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL",
                    "6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => "
                    "6 FHTLT",
                    "15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW",
                    "13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW",
                    "5 BMBT => 4 WPTQ",
                    "189 ORE => 9 KTJDG",
                    "1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP",
                    "12 VRPVC, 27 CNZTR => 2 XDBXC",
                    "15 KTJDG, 12 BHXH => 5 XCVML",
                    "3 BHXH, 2 VRPVC => 7 MZWV",
                    "121 ORE => 7 VRPVC",
                    "7 XCVML => 6 RJRHP",
                    "5 BHXH, 4 VRPVC => 5 LTCX",
                ],
                2210736,
            ),
        ],
    )
    def test_day14a_solve(self, input_data, expected_result):
        input_lines = "\n".join(input_data)
        solution = Day14PartA()
        result = solution.solve(input_lines)
        assert result == expected_result

    def test_day14a_data(self):
        """ Result we got when we did the real solution """
        solution = Day14PartA()
        res = solution("day_14/day14.txt")
        assert res == 1065255
