from adventofcode2019.solutions.day12 import Day12PartA, Galaxy, Moon


class TestDay12PartA:
    def test_moon(self):
        input_string = "<x=-1, y=0, z=2>"
        moon = Moon.parse_input(input_string)
        assert moon.x == -1
        assert moon.y == 0
        assert moon.z == 2

        assert repr(moon) == "pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>"

    def test_creation(self):
        input_strings = [
            "<x=-1, y=0, z=2>",
            "<x=2, y=-10, z=-7>",
            "<x=4, y=-8, z=8>",
            "<x=3, y=5, z=-1>",
        ]
        input_string = "\n".join(input_strings)
        galaxy = Galaxy()
        galaxy.create_moons(input_string)

        assert len(galaxy.moons) == 4
        assert (
            repr(galaxy.moons[0])
            == "pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>"
        )
        # Let's assume the rest is the same and that creating the Moons worked
        galaxy.step()

        step_1_pos = [
            "pos=<x=  2, y= -1, z=  1>, vel=<x=  3, y= -1, z= -1>",
            "pos=<x=  3, y= -7, z= -4>, vel=<x=  1, y=  3, z=  3>",
            "pos=<x=  1, y= -7, z=  5>, vel=<x= -3, y=  1, z= -3>",
            "pos=<x=  2, y=  2, z=  0>, vel=<x= -1, y= -3, z=  1>",
        ]
        for i, expected_position in enumerate(step_1_pos):
            assert repr(galaxy.moons[i]) == expected_position

        # Step another 9 times to get to step 10:
        galaxy.step_multi(9)
        step_10_pos = [
            "pos=<x=  2, y=  1, z= -3>, vel=<x= -3, y= -2, z=  1>",
            "pos=<x=  1, y= -8, z=  0>, vel=<x= -1, y=  1, z=  3>",
            "pos=<x=  3, y= -6, z=  1>, vel=<x=  3, y=  2, z= -3>",
            "pos=<x=  2, y=  0, z=  4>, vel=<x=  1, y= -1, z= -1>",
        ]
        for i, expected_position in enumerate(step_10_pos):
            assert repr(galaxy.moons[i]) == expected_position

        assert galaxy.get_total_energy() == 179

    def test_day12a_data(self):
        """ Result we got when we did the real solution """
        solution = Day12PartA()
        res = solution("day_12/day12.txt")
        assert res == 5350
