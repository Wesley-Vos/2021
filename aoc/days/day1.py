from aoc.util.Day import Day


class Day1(Day):
    depths = None

    def __init__(self, filename):
        super().__init__(filename)
        self.depths = list(map(int, self.data))

    @staticmethod
    def count_increasing_items(data, window):
        return sum(cur > prev for prev, cur in zip(data, data[window:]))

    def solve_part1(self):
        return self.count_increasing_items(self.depths, 1)

    def solve_part2(self):
        return self.count_increasing_items(self.depths, 3)


def main():
    day1 = Day1("day1.txt")
    day1.run()


if __name__ == "__main__":
    main()
