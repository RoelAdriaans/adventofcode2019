import pytest

from adventofcode2019.solutions.day08 import Day08PartB


class TestDay08PartB:
    @pytest.mark.parametrize(
        ("input_list", "expected_result"),
        [([0, 1, 2, 0], 0), ([2, 1, 2, 0], 1), ([2, 2, 1, 0], 1), ([2, 2, 2, 0], 0)],
    )
    def test_compute_per_pixel(self, input_list, expected_result):
        result = Day08PartB._compute_per_pixel(input_list)
        assert result == expected_result

    def test_compose_image(self):
        """ Get the number of digits per layer"""
        solution = Day08PartB()
        solution.load_image(image_data="0222112222120000", width=2, height=2)
        assert len(solution.frames) == 4

        result = solution.get_computed_image()
        assert result == [0, 1, 1, 0]

        assert solution.printable_image(result) == "01\n10"

    def test_day08a_data(self):
        """ Result we got when we did the real solution """
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        expected = (
            "■  ■  ■■  ■■■   ■■  ■■■■ \n"
            "■  ■ ■  ■ ■  ■ ■  ■ ■    \n"
            "■■■■ ■    ■■■  ■    ■■■  \n"
            "■  ■ ■ ■■ ■  ■ ■    ■    \n"
            "■  ■ ■  ■ ■  ■ ■  ■ ■    \n"
            "■  ■  ■■■ ■■■   ■■  ■    "
        )
        # Readble as HGBCF
        assert res == expected
