from util.Day import Day
from util.Submarine import Submarine


class Day3(Day):
    commands = None
    submarine = None

    def __init__(self, filename):
        super().__init__(filename)
        print(self.data)

    def solve_part1(self):
        return 0

    def solve_part2(self):
        return 0


def main():
    day = Day3("day3.txt")
    day.run()


if __name__ == "__main__":
    main()
