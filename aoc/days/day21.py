from aoc.util.Day import Day

import re

RE_PATTERN = r"Player (\d*) starting position: (\d*)"


class DeterministicDice:
    def __init__(self, size):
        self.rolls = 0
        self.res = 0
        self.size = size
    
    def roll(self):
        self.res = new if (new := self.res + 1) <= self.size else new % self.size
        self.rolls += 1
        return self.res
    

class DiracDice:
    def __init__(self, data, dice, win):
        self.dice = dice
        self.num_players = len(data)
        self.pos = []
        self.scores = []
        self.win = win
        for i, row in enumerate(data):
            player, pos = re.findall(RE_PATTERN, row, re.MULTILINE)[0]
            self.pos.append(int(pos))
            self.scores.append(0)
    
    def play(self):
        while True:
            for i in range(self.num_players):
                new = (self.pos[i] + sum(self.dice.roll() for _ in range(3))) % 10
                self.pos[i] = 10 if new == 0 else new
                self.scores[i] += self.pos[i]
                if self.scores[i] >= self.win:
                    return self.scores[(i + 1)%self.num_players] * self.dice.rolls
        return 0


class Day21(Day):
    def __init__(self, filename):
        pass
        super().__init__(filename)
        dice100 = DeterministicDice(100)
        self.game = DiracDice(self.data, dice100, 1000)

    def solve_part1(self):
        return self.game.play()

    def solve_part2(self):
        return None


def main():
    day = Day21("day21.in")
    day.run()


if __name__ == "__main__":
    main()
