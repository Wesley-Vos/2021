from util.Day import Day
from util.Submarine import Submarine, AimedSubmarine


class Day3(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.report = self.data

    def solve_part1(self):
        submarine = Submarine()
        return submarine.calculate_power_consumption(self.report)

    def solve_part2(self):
        submarine = Submarine()
        return submarine.calculate_life_support_rating(self.report)


def main():
    day3 = Day3("test/day3.txt")
    day3.run()


if __name__ == "__main__":
    main()
