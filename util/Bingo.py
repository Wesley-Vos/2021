class Bingo:
    class Card:
        def __init__(self, data):
            self._data = [list(map(int, d.split())) for d in data]
            self.won = False

        def check(self, draw):
            if self.won:
                return False

            for i, row in enumerate(self._data):
                for j, num in enumerate(row):
                    if num == draw:
                        self._data[i][j] = 0
                        hor = len(set(self._data[i])) == 1
                        vert = len(set([self._data[idx][j] for idx in range(0, 5)])) == 1
                        if vert or hor:
                            self.won = True
                            return True
            return False

        def sum_unmarked(self):
            return sum(sum(n for n in row) for row in self._data)

    def __init__(self, data):
        data = [d for d in data if d != '']
        self._numbers = [int(d) for d in data[0].split(",")]
        self._cards = [self.Card(data[i:i+5]) for i in range(1, len(data), 5)]

    def play(self, first):
        last_val = 0
        for draw in self._numbers:
            for card in self._cards:
                if card.check(draw):
                    if first:
                        return card.sum_unmarked()*draw
                    else:
                        last_val = card.sum_unmarked()*draw
        return last_val
