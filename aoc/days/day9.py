from aoc.util.Day import Day
from math import prod


class LavaTubes:
    def __init__(self, data):
        self.data = [list(map(int, list(d))) for d in data]
        self.len_x = len(self.data[0])
        self.len_y = len(self.data)
        self.visited = [[False for _ in row] for row in self.data]

    def low_point(self, i, j):
        neighbours = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        return all(self.data[i][j] < self.data[i1][j1] for i1, j1 in neighbours if self.len_y > i1 >= 0 and self.len_x > j1 >= 0)

    def calc_low_points(self):
        return sum(sum((h + 1) * self.low_point(i, j) for j, h in enumerate(row)) for i, row in enumerate(self.data))

    def calc_basins(self):
        res = []
        for i, row in enumerate(self.data):
            for j, h in enumerate(row):
                if self.low_point(i, j):
                    val = self.get_basin_size(i, j)
                    res.append(val)
        res.sort(reverse=True)
        return prod(res[0:3])

    def get_basin_size(self, i, j):
        if not (self.len_y > i >= 0 and self.len_x > j >= 0) or self.visited[i][j]:
            return 0
        self.visited[i][j] = True

        size = 0
        if self.len_y > i >= 0 and self.len_x > j >= 0 and self.data[i][j] < 9:
            size = 1
            size += self.get_basin_size(i, j - 1)
            size += self.get_basin_size(i, j + 1)
            size += self.get_basin_size(i - 1, j)
            size += self.get_basin_size(i + 1, j)
        return size


class Day9(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.lt = LavaTubes(self.data)

    def solve_part1(self):
        return self.lt.calc_low_points()

    def solve_part2(self):
        return self.lt.calc_basins()


def main():
    day = Day9("day9.in")
    day.run()


if __name__ == "__main__":
    main()
