from aoc.util.Bingo import Bingo
from aoc.util.Day import Day


class Day4(Day):
    numbers = None
    cards = None

    def __init__(self, filename):
        super().__init__(filename)
        self.bingo = Bingo(self.data)
        
    def solve_part1(self):
        return self.bingo.play(True)

    def solve_part2(self):
        return self.bingo.play(False)


def main():
    day = Day4("day4.txt")
    day.run()


if __name__ == "__main__":
    main()
