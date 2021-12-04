# Advent of Code 2021

Written in Python 3.10 following the Object-Oriented Programming paradigm and tricks from functional programming.
## Days
### Day 1 - Increasing numbers

### Day 2 - Depth mapping

### Day 3 - Diagnostics

### Day 4 - Bingo
The game at Day 4 was playing Bingo with a squid. Given the input of drawn numbers and all bingo cards.
The program has to find the card that as first (or last) has one full row. The result is the sum of unmarked numbers
on the winning card multiplied by the last drawn number.
```python
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
```

***

## Skeleton classes

### Day
This class is the base for all the days. It reads the input file on initialization
It has two base abstract methods that should be implemented by the actual Day class. 
The solve part 1 and 2 methods are printed on request by the run method.
```python
class Day:
    data = None

    def __init__(self, filename):
        self._read(filename)

    def _read(self, filename):
        with open(f"input/{filename}") as input_file:
            self.data = input_file.read().splitlines()

    def solve_part1(self):
        return "Answer part 1: still unknown"

    def solve_part2(self):
        return "Answer part 2: still unknown"

    def run(self):
        print(f"Answer part 1: {self.solve_part1()}")
        print(f"Answer part 2: {self.solve_part2()}")
```

### Submarine
*Used in day 2 and 3*

The submarine class is the base class of the Submarine used this year. The submarine has a position
and diagnostics. The submarine can move in three different directions, forward, up and down. The implementation of these movements
are differing for the standard submarine and the aimed submarine which is an extended class of this base class.
```python
class Submarine:
    class Position:
        def __init__(self):
            self.x = 0
            self.depth = 0

    position = None
    diagnostics = None

    def __init__(self):
        self.position = self.Position()

    def move(self, direction, amount):
        match direction:
            case "forward":
                self.position.x += amount
            case "up":
                self.position.depth -= amount
            case "down":
                self.position.depth += amount

    def insert_diagnostics_report(self, report):
        self.diagnostics = self.Diagnostics(report)

    def calculate_power_consumption(self):
        gamma, terra = self.diagnostics.analyse_power()
        return gamma * terra

    def calculate_life_support_rating(self):
        oxygen, co2 = self.diagnostics.analyse_living()
        return oxygen * co2
```

### Diagnostics
The diagnostics subclass of the submarine is used in day 3 for interpreting the diagnostics report and get
the gamma, terra, oxygen and co2scrubber coefficients. 
```python
class Diagnostics:
    def __init__(self, report):
        self.report = report

    @staticmethod
    def max_tied(a, b, tie):
        return tie if a == b else (a if tie else b)

    @staticmethod
    def _get_commons(report):
        report = zip(*map(list, report))
        report = list(map(lambda r: tuple(map(int, r)), report))
        most_common = [max(set(bit), key=bit.count) for bit in report]
        least_common = [min(set(bit), key=bit.count) for bit in report]
        return most_common, least_common

    @staticmethod
    def _bitstring_to_int(bitstring):
        return int(''.join(map(str, bitstring)), 2)

    def _filter_report(self, most):
        filtered_report = [list(map(int, bit)) for bit in self.report]

        idx = 0
        while len(filtered_report) > 1:
            # print("Before filter", filtered_report)
            most_common, least_common = self._get_commons(filtered_report)
            check = self.max_tied(most_common[idx], least_common[idx], int(most))
            # print(check)
            filtered_report = [bit for bit in filtered_report if bit[idx] == check]
            # print("After filter", filtered_report)
            idx += 1
        return filtered_report[0]

    def analyse_power(self):
        most_common, least_common = self._get_commons(self.report)

        gamma = self._bitstring_to_int(most_common)
        terra = self._bitstring_to_int(least_common)
        return gamma, terra

    def analyse_living(self):
        filter_most = self._filter_report(True)
        filter_least = self._filter_report(False)

        oxygen = self._bitstring_to_int(filter_most)
        co2 = self._bitstring_to_int(filter_least)
        return oxygen, co2
```