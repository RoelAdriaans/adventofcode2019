import math
import typing
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Dict, List, NamedTuple

from adventofcode2019.utils.abstract import FileReaderSolution


class Chemical(NamedTuple):
    consumable: int
    name: str


class Recipe(NamedTuple):
    inputs: List[Chemical]
    output: Chemical

    @staticmethod
    def parse_recipe_string(input_string: str) -> "Recipe":
        """Parse a string as a Recipe and return a new Recipe.

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
        """Compute what we need for `n` units of `output` and return this as a Dict.
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

    def create_nodes(self) -> Node:
        """
        Create all the `Node` instances for the current recipes and return the
        root_node with all the childeren in the Edges
        """
        nodes = {}
        root_node: Node
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

        return root_node

    def resolve_tree(self) -> List[Node]:
        """ Resolve the tree and return a list of nodes in order to process them."""
        root_node = self.create_nodes()
        resolved: List[Node] = []
        self.dep_resolve(root_node, resolved, [])
        return resolved

    def ore_needed_for_n_fuel(self, n=1) -> int:
        """ Compute how many ORE we need for `n` fuel object"""
        # Do a recursive from FUEL to ORE
        resolved = self.resolve_tree()

        counter: typing.Counter = Counter()
        # See what we need. We need to start revedsed, because we do not know how many
        # ORE we need for 1 FUEL
        for node in reversed(resolved):
            if len(node.edges) == 0:
                # Ore, doesn't need anything
                continue

            if node.name == "FUEL":
                qty = n
            else:
                qty = counter[node.name]

            requirements_for_node = self._get_requirement_for_one(node.name, qty)
            counter.update(requirements_for_node)

        return counter["ORE"]


class Day14:
    pass


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        factory = NanoFactory()
        factory.read_input(input_data)
        ore = factory.ore_needed_for_n_fuel()
        return ore


class Day14PartB(Day14, FileReaderSolution):
    def binary_search(
        self, search: int = 1_000_000_000_000, factory: NanoFactory = None
    ) -> int:
        """
        Implement a binary search to search for the magic number
        :param search: The number we want to his
        :param factory: The NanoFactory that generates the ore
        :return: Number if `fuel` that can be created from `search` ore.
        """
        if not factory:
            return -1

        low = 1
        middle = 0
        high = search
        found = False
        ore_needed = 0

        while low < high and not found:
            middle = (low + high + 1) // 2
            ore_needed = factory.ore_needed_for_n_fuel(middle)
            if ore_needed == search:
                return middle
            else:
                if search < ore_needed:
                    high = middle - 1
                else:
                    low = middle

        # Our result may not overshoot the search, remove one if too high
        if ore_needed > search:
            middle -= 1
        return middle

    def solve(self, input_data: str) -> int:
        factory = NanoFactory()
        factory.read_input(input_data)
        res = 1_000_000_000_000

        res = self.binary_search(res, factory)
        return res
