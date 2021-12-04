from util.Day import Day
from util.Submarine import Submarine


class Day4(Day):
    numbers = None
    cards = None
    submarine = None

    def __init__(self, filename):
        super().__init__(filename)
        self.bingo = Bingo(self.data)
        

    def solve_part1(self):
        return self.bingo.play(True)

    def solve_part2(self):
        return self.bingo.play(False)

class Bingo:
    class Card:
        def __init__(self, data):
            self._data = [list(map(int, d.split())) for d in data]
            self.won = False
            #print(self._data)
            #self._remain = 25
    
        def check(self, draw):
            if self.won:
                return False
            
            for i, row in enumerate(self._data):
                for j, num in enumerate(row):
                    #print(num, draw)
                    if num == draw:
                        #print("found")
                        self._data[i][j] = -1
                        #self._remain -= 1
                        hor = len(set(self._data[i])) == 1
                        vert = len(set([self._data[idx][j] for idx in range(0, 5)])) == 1
                        if vert or hor:
                            self.won = True
                            return True
            return False
            
        def sum_unmarked(self):
            sum_val = 0
            for row in self._data:
                sum_val += sum(n for n in row if n != -1)
            return sum_val

    def __init__(self, data):
        data = [d for d in data if d != '']
        self.numbers = list(map(int, data[0].split(",")))
        self.cards = [self.Card(data[i:i+5]) for i in range(1, len(data), 5)]

    def play(self, first):
        last_val = 0
        for draw in self.numbers:
            for card in self.cards:
                if card.check(draw):
                    if first:
                        return card.sum_unmarked()*draw
                    else:
                        last_val = card.sum_unmarked()*draw
        return last_val
        

def main():
    day = Day4("day4.txt")
    day.run()


if __name__ == "__main__":
    main()
