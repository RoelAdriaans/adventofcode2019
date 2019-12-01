from utils.abstract import FileReaderSolution


class Day01:
    @staticmethod
    def compute_fuel(mass):
        """
        Fuel required to launch a given module is based on its mass.
        Specifically, to find the fuel required for a module, take its mass,
        divide by three, round down, and subtract 2.
        """
        fuel = mass // 3 - 2
        return fuel

    def compute_including_extra_fuel(self, mass):
        total_fuel = 0
        extra_fuel = mass
        # fuel = self.compute_fuel(mass)
        while True:
            # Compute the fuel for this fuel
            extra_fuel = self.compute_fuel(extra_fuel)
            if extra_fuel <= 0:
                return total_fuel
            else:
                total_fuel += extra_fuel


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        fuel = [Day01.compute_fuel(int(mass)) for mass in input_data.splitlines()]
        return sum(fuel)


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        extra_fuel = []
        for module in input_data.splitlines():
            extra_fuel.append(self.compute_including_extra_fuel(int(module)))
        return sum(extra_fuel)
