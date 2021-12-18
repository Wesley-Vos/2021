from aoc.util.Day import Day


class Homework:
    def __init__(self, data):
        self.numbers = []
        for row in data:
            print(row)

    def parse(self, row):
        for char in row:




class SnailNumber:
    left = None
    right = None

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _parse(self, data):
        pass

    def add(self, other):
        return SnailNumber(self, other)

    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"


class Day18(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.homework = Homework(self.data)

    def solve_part1(self):
        return None

    def solve_part2(self):
        return None


def main():
    day = Day18("test/day18.in")
    day.run()


if __name__ == "__main__":
    main()
