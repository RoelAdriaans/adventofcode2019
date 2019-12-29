import math

from collections import defaultdict, Counter
from typing import List, NamedTuple, Dict
from utils.abstract import FileReaderSolution
from dataclasses import dataclass


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


@dataclass
class Node:
    name: str
    edges: list

    def __init__(self, name: str):
        self.name = name
        self.edges = []

    def add_edge(self, node: "Node"):
        self.edges.append(node)


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

        return required

    def dep_resolve(self, node: Node, resolved: List, unresolved: List):
        """
        Resolve the order in which we need to process out recipe.
        Does checks for circular dependencies ( A->B->C->A )
        Code from https://www.electricmonk.nl

        :param node: Root node
        :param resolved: List of resolved nodes
        :param unresolved: List of onresolved nodes
        :return:
        """
        unresolved.append(node)
        for edge in node.edges:
            if edge not in resolved:
                if edge in unresolved:
                    raise Exception(
                        f"Circular reference detected: {node.name} -> {edge.name}"
                    )
                self.dep_resolve(edge, resolved, unresolved)
        resolved.append(node)
        unresolved.remove(node)

    def ore_needed_for_one_fuel(self) -> int:
        """ Compute how many ORE we need for ONE fuel object"""
        # Do a recursive from FUEL to ORE
        fuel = self._get_requirement_for_one("FUEL", 1)

        # Do something.. :(
        # What do I need:
        # Fuel: A: 7, E: 1
        # For 7 A: 70 ORE
        # Add checks for what we need to produce (A, B, C, D, E, FUEL), and what we can
        # produce

        # Let's create the nodes, and see if if this works if we can shoehorn this into
        # the main algoritm.
        nodes = {}
        root_node = False
        # Firstly, Creates nodes
        for key, recipe in self.recipes.items():
            node = Node(key)
            nodes[key] = node
            if key == "FUEL":
                root_node = node

        # Since ORE isn't really output but the result, we add it by hand
        nodes["ORE"] = Node("ORE")

        # Next, create all the Edges
        for key, recipe in self.recipes.items():
            for input_recipe in recipe.inputs:
                input_recipe_node = nodes[input_recipe.name]
                nodes[key].add_edge(input_recipe_node)


        resolved = []
        self.dep_resolve(root_node, resolved, [])
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
