from util.Day import Day
from util.Submarine import Submarine, AimedSubmarine


class Day2(Day):
    commands = None

    class Command:
        direction = None
        amount = 0

        def __init__(self, row):
            row = row.split(" ")
            self.direction = row[0]
            self.amount = int(row[1])

    def __init__(self, filename):
        super().__init__(filename)
        self.commands = list(map(self.Command, self.data))

    def _solve_partX(self, submarine):
        for command in self.commands:
            submarine.move(command.direction, command.amount)
        return submarine.position.x * submarine.position.depth

    def solve_part1(self):
        return self._solve_partX(Submarine())

    def solve_part2(self):
        return self._solve_partX(AimedSubmarine())


def main():
    day2 = Day2("day2.txt")
    day2.run()


if __name__ == "__main__":
    main()
