from adventofcode2019.solutions.infi import Infi


class TestInfi:
    def test_infi_example(self):
        infi = Infi("example.json")

        assert len(infi.flats) == 6
        assert len(infi.jumps) == 4

        result = infi.when_does_santa_fell_down(infi.jumps)
        assert result == 4

    def test_infi_data(self):
        infi = Infi("infi.json")

        result = infi.when_does_santa_fell_down(infi.jumps)
        assert result == 12
