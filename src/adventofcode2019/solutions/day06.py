from typing import List

from anytree import Node, Walker  # type: ignore

from adventofcode2019.utils.abstract import FileReaderSolution


class Day06:
    def __init__(self):
        self.nodes = {}
        self.root_node = None

    @staticmethod
    def parse_lines(input_lines) -> List:
        orbits = []
        for line in input_lines:
            a, b = line.split(")")
            orbits.append((a, b))
        return orbits

    def create_nodes(self, orbits):
        # Create all the nodes
        for node in orbits:
            root, child = node[0], node[1]
            root_node = self.nodes.get(root)
            if not root_node:
                root_node = Node(name=root)
                self.nodes[root] = root_node

            child_search_node = self.nodes.get(child)
            if child_search_node:
                child_search_node.parent = root_node
            else:
                child_node = Node(name=child, parent=root_node)
                self.nodes[child] = child_node

        # Find the root node
        self.root_node = [node for node in self.nodes.values() if node.is_root]
        if len(self.root_node) >= 2:
            raise ValueError("Too much roots! Found: {len(self.root_node)}")

    def find_distance_between_nodes(self, node_from: str, node_to: str) -> int:
        """ Find the distance between nodes """
        # We are on the node we want to compute from, so we start with our parent
        from_node = self.nodes[node_from].parent
        to_node = self.nodes[node_to].parent
        w = Walker()
        walk = w.walk(from_node, to_node)

        # Walk 0 contains the nodes to go up,
        # Walk 1 contains the common node, we can ignore that one,
        # Walk 2 contains the nodes to go down.
        return len(walk[0]) + len(walk[2])


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        # Parse input
        input_lines = input_data.splitlines()
        orbits = self.parse_lines(input_lines)
        self.create_nodes(orbits)
        result = sum([node.depth for node in self.nodes.values()])
        return result


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        # Parse input
        input_lines = input_data.splitlines()
        orbits = self.parse_lines(input_lines)
        self.create_nodes(orbits)
        res = self.find_distance_between_nodes("YOU", "SAN")
        return res
