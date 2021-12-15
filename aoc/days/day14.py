from collections import defaultdict

from aoc.util.Day import Day


class PolymerBuilder:
    def __init__(self, start, mapping):
        self.mapping = mapping
        self.pairs = defaultdict(lambda: 0)
        self.chars = defaultdict(lambda: 0, [(start[0], 1)])
        for i, j in zip(start, start[1:]):
            self.pairs[i + j] += 1
            self.chars[j] += 1

    def build(self, n):
        for _ in range(n):
            for (i, j), c in self.pairs.copy().items():
                mid = self.mapping[i + j]
                self.pairs[i + j] -= c
                self.pairs[i + mid] += c
                self.pairs[mid + j] += c
                self.chars[mid] += c

    def get_commons_diff(self):
        return max(self.chars.values()) - min(self.chars.values())


class Day14(Day):
    def __init__(self, filename):
        super().__init__(filename)
        start, mapping = self._process_input()
        self.polymer = PolymerBuilder(start, mapping)

    def _process_input(self):
        start, _, *mapping = self.data
        return start, dict(r.split(" -> ") for r in mapping)

    def solve_part1(self):
        self.polymer.build(10)
        return self.polymer.get_commons_diff()

    def solve_part2(self):
        self.polymer.build(30)
        return self.polymer.get_commons_diff()


def main():
    day = Day14("day14.in")
    day.run()


if __name__ == "__main__":
    main()
