from aoc.util.Day import Day


class Day7(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.data = list(map(int, self.data[0].split(",")))

    def calc(self, linear_fuel=True):
        return int(min(sum(diff if (diff := abs(d - i)) and linear_fuel else diff*(diff + 1)/2 for d in self.data) for i in range(min(self.data), max(self.data) + 1)))

    def solve_part1(self):
        return self.calc()

    def solve_part2(self):
        return self.calc(False)


def main():
    day = Day7("day7.in")
    day.run()


if __name__ == "__main__":
    main()
