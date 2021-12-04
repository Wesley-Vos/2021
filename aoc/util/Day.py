class Day:
    data = None

    def __init__(self, filename):
        self._read(filename)

    def _read(self, filename):
        with open(f"input/{filename}") as input_file:
            self.data = input_file.read().splitlines()

    def solve_part1(self):
        return "Answer part 1: still unknown"

    def solve_part2(self):
        return "Answer part 2: still unknown"

    def run(self):
        print(f"Answer part 1: {self.solve_part1()}")
        print(f"Answer part 2: {self.solve_part2()}")
