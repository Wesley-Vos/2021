from util.Day import Day
from util.Submarine import Submarine


class Day3(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.submarine = Submarine()
        self.submarine.insert_diagnostics_report(self.data)

    def solve_part1(self):
        return self.submarine.calculate_power_consumption()

    def solve_part2(self):
        return self.submarine.calculate_life_support_rating()


def main():
    day3 = Day3("test/day3.txt")
    day3.run()


if __name__ == "__main__":
    main()
