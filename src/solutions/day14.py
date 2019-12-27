import math

from collections import defaultdict, Counter
from typing import List, NamedTuple, Dict
from utils.abstract import FileReaderSolution


class Chemical(NamedTuple):
    consumable: int
    name: str


class Recipe(NamedTuple):
    inputs: List[Chemical]
    output: Chemical

    @staticmethod
    def parse_recipe_string(input_string: str) -> "Recipe":
        """ Parse a string as a Recipe and return a new Recipe.

        :param input_string: Input string, for example "1 A, 2 B, 3 C => 2 D
        :return Recipe object
         """
        inputs, outputs = input_string.strip().split(" => ")

        input_parts = inputs.split(",")

        input_chemicals = []

        for input_part in input_parts:
            consumable, name = input_part.strip().split(" ")
            input_chemicals.append(
                Chemical(consumable=int(consumable), name=name.strip())
            )

        consumable, name = outputs.split(" ")
        output_chemical = Chemical(consumable=int(consumable), name=name)

        new_recipe = Recipe(inputs=input_chemicals, output=output_chemical)
        return new_recipe


class NanoFactory:
    warehouse: defaultdict
    recipes: Dict[str, Recipe]

    def __init__(self):
        self.warehouse = defaultdict(int)
        self.recipes = {}

    def read_input(self, input_lines: str):
        for line in input_lines.splitlines():
            recipe = Recipe.parse_recipe_string(line)
            self.recipes[recipe.output.name] = recipe

    def _get_requirement_for_one(self, output: str, n: int) -> Dict[str, int]:
        """ Compute what we need for `n` units of `output` and return this as a Dict.
        For example, with the recipe `4 C, 1 A => 1 CA`, when we need 4 of `CA`, return
        {"C": 16, "A": 4}
        """
        result = {}
        output_recipe = self.recipes.get(output)
        if output_recipe:
            # We can only create multiples, eg if `mutiple` is 10, and `n` is 15,
            # we have to create 20 units.
            multiple_required = output_recipe.output.consumable
            number_needed = math.ceil(n / multiple_required)

            for input_recipe in output_recipe.inputs:
                result[input_recipe.name] = input_recipe.consumable * number_needed
        return result

    def _get_requirement_for_multiple(self, required: Dict):
        """
        Computer the requirements for multiple outputs, recursive.
        :param outputs:
        :return:
        """
        for chemical, num in required.copy().items():
            required_for_chemical = self._get_requirement_for_one(chemical, num)
            for name, qty in required_for_chemical.items():
                required[name] = required.get(name, 0) + qty

            recursive_req = self._get_requirement_for_multiple(required_for_chemical)
            for name, qty in recursive_req.items():
                required[name] = required.get(name, 0) + qty

            # required.update(recursive_req)

        return required

    def ore_needed_for_one_fuel(self) -> int:
        """ Compute how many ORE we need for ONE fuel object"""
        # Do a recursive from FUEL to ORE
        fuel = self._get_requirement_for_one("FUEL", 1)
        res = self._get_requirement_for_multiple(fuel)

        return 0


class Day14:
    pass


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        factory = NanoFactory()
        factory.read_input(input_data)
        ore = factory.ore_needed_for_one_fuel()
        return ore


class Day14PartB(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
