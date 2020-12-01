"""
Advent of Code puzzle of infi: https://aoc.infi.nl/
"""
import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


@dataclass
class Santa:
    current_location: Point


class Infi:
    filename: str
    flats: Dict[int, Point]
    jumps: deque
    santa: Santa

    def __init__(self, filename: str = "info.json"):
        """
        Initialize a new Infi AOC 2019 puzzle.
        :param filename: Filename with the data we will parse
        """
        self.filename = filename
        self._load_data()

    def _load_data(self):
        """ Open the file and parse the json data inside the file """
        root_dir = Path(__file__).parent.parent
        # with open(root_dir / "solutions" / "data" / input_file) as f:

        with open(root_dir / "solutions" / "data" / "infi" / self.filename, "r") as f:
            data = json.load(f)

        self.flats = {}
        for flat in data["flats"]:
            point = Point(flat[0], flat[1])
            self.flats[point.x] = point

        self.jumps = deque()
        for sprong in data["sprongen"]:
            point = Point(sprong[0], sprong[1])
            self.jumps.append(point)

    def when_does_santa_fell_down(self, jumps: deque) -> int:
        """
        Let's see how well Santa does, return how many jumps he can make
        """
        counter = 0

        # Santa will start at the first flat
        self.santa = Santa(current_location=self.flats[min(self.flats.keys())])
        while self.santa.current_location.y >= 1:
            jump = jumps.popleft()
            # We always move one to the right, and add the latteral movement from
            # the jump
            new_x = self.santa.current_location.x + jump.x + 1
            new_y = self.santa.current_location.y + jump.y

            new_flat = self.flats.get(new_x)

            # Let's see if he jumped high enough:
            if not new_flat or new_y < new_flat.y:
                # new height is lower then the current height of the flat,
                # falling down :(
                self.santa.current_location = Point(x=new_x, y=0)
            else:
                # Santa fell on the roof
                self.santa.current_location = Point(x=new_x, y=new_flat.y)

            counter += 1
        return counter
