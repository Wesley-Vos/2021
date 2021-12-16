import sys

from aoc.util.Day import Day

INT_MAX = 1000000000


class Chiton:
    def __init__(self, data):
        self.grid = {(x, y): {"val": int(val), "min": INT_MAX} for y, row in enumerate(data) for x, val in enumerate(row)}
        self.des = (len(data[0]) - 1, len(data) - 1)
        self.size = len(data)

    def new_enlarged_grid(self, size=5):
        for x, y in list(self.grid.keys()):
            self.grid[(x, y)]["min"] = INT_MAX
            for i in range(1, size):
                new_x, new_y = x + i*self.size, y + i*self.size
                val = val - 9 if (val := self.grid[(x, y)]["val"] + i) > 9 else val
                self.grid[(new_x, y)] = {"val": val, "min": INT_MAX}
        for x, y in list(self.grid.keys()):
            for i in range(1, size):
                new_x, new_y = x + i*self.size, y + i*self.size
                val = val - 9 if (val := self.grid[(x, y)]["val"] + i) > 9 else val
                self.grid[(x, new_y)] = {"val": val, "min": INT_MAX}
        self.size = self.size * size
        self.des = (self.size - 1, self.size - 1)

    def min_path(self, pos=(0, 0)):
        x, y = pos
        val = 0 if pos == (0, 0) else self.grid[pos]["val"]
        min_val = self.grid[pos]["min"]
        if pos == self.des:
            return val
        if min_val != INT_MAX:
            return min_val

        neighbours = {(x + dx, y + dy) for dx, dy in {(0, 1), (1, 0)}}
        min_val = min(val + self.min_path(n) for n in neighbours if n in self.grid)
        self.grid[pos]["min"] = min_val
        return min_val


class Graph:
    def __init__(self, data):
        self.grid = {(x, y): {"val": int(val), "min": INT_MAX} for y, row in enumerate(data) for x, val in enumerate(row)}
        self.V = self.

    def dijkstra(self, pos=(0, 0)):
        pass


class Day15(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.chiton = Chiton(self.data)

    def solve_part1(self):
        return self.chiton.min_path()

    def solve_part2(self):
        self.chiton.new_enlarged_grid()
        return self.chiton.min_path()


def main():
    sys.setrecursionlimit(4000)
    day = Day15("day15.in")
    day.run()


if __name__ == "__main__":
    main()
