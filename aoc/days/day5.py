from aoc.util.Day import Day
import re


class HydroThermalVents:
    def __init__(self, data):
        self.visits = {}
        self.data = data

    def check(self, straight_only=True):
        reg_pattern = r"(\d*),(\d*) -> (\d*),(\d*)"
        for row in self.data:
            match = re.findall(reg_pattern, row, re.MULTILINE)[0]
            x1, y1, x2, y2 = map(int, match)

            if x1 == x2:
                y_range = range(y1, y2 + 1) if y2 > y1 else range(y2, y1 + 1)
                for y in y_range:
                    self.visits[(x1, y)] = 1 + self.visits.get((x1, y), 0)
            elif y1 == y2:
                x_range = range(x1, x2 + 1) if x2 > x1 else range(x2, x1 + 1)
                for x in x_range:
                    self.visits[(x, y1)] = 1 + self.visits.get((x, y1), 0)
            elif not straight_only and abs(x1 - x2) == abs(y1 - y2):
                amount = abs(x1 - x2)
                x_range = list(range(x1, x2 + 1)) if x2 > x1 else sorted(list(range(x2, x1 + 1)), reverse=True)
                y_range = list(range(y1, y2 + 1)) if y2 > y1 else sorted(list(range(y2, y1 + 1)), reverse=True)

                for i in range(0, amount + 1):
                    x, y = x_range[i], y_range[i]
                    self.visits[(x, y)] = 1 + self.visits.get((x, y), 0)

        return len([cnt for cnt in self.visits.values() if cnt >= 2])


class Day5(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.htv = HydroThermalVents(self.data)
        
    def solve_part1(self):
        return self.htv.check()

    def solve_part2(self):
        return self.htv.check(False)


def main():
    day = Day5("day5.in")
    day.run()


if __name__ == "__main__":
    main()
