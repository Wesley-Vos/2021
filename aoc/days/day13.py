from aoc.util.Day import Day
from collections import defaultdict
import re


class Paper:
    def __init__(self, data):
        self.grid = defaultdict(lambda: 0)
        self.size = {"x": 0, "y": 0}
        self.fold_instructions = []
        for row in filter(lambda r: r != "", data):
            if row[0].isnumeric():
                x, y = map(int, row.split(","))
                self.size["x"] = max(self.size["x"], x + 1)
                self.size["y"] = max(self.size["y"], y + 1)
                self.grid[(x, y)] = 1
            else:
                reg_pattern = r"fold along ([xy])=(\d*)"
                xy, val = re.findall(reg_pattern, row, re.MULTILINE)[0]
                self.fold_instructions.append({'x': int(val) if xy == 'x' else None, 'y': int(val) if xy == 'y' else None})

    def __str__(self):
        out = ""
        for y in range(self.size['y']):
            out += f"{y}: "
            for x in range(self.size['x']):
                out += "  " if not self.grid[(x, y)] else "##"
            out += "\n"
        return out

    def fold(self, x_fold, y_fold):
        print(f"Fold along x={x_fold}, y={y_fold}, size={self.size}")
        if x_fold is not None:
            dx = x_fold
            for y in range(self.size['y']):
                for x in range(dx, self.size['x']):
                    opp = (self.size['x'] - x - 1, y)
                    #print((x, y), opp)
                    self.grid[opp] = self.grid[(x, y)] or self.grid[opp]
                    self.grid.pop((x, y), None)
            self.size['x'] = x_fold

        if y_fold is not None:
            dy = y_fold
            for y in range(dy, self.size['y']):
                for x in range(self.size['x']):
                    opp = (x, self.size['y'] - y - 1)
                    #print((x, y), opp)
                    self.grid[opp] = self.grid[(x, y)] or self.grid[opp]
                    self.grid[(x, y)] = 0
            self.size['y'] = y_fold

    def cnt_dots(self):
        return sum(1 for val in self.grid.values() if val)


class Day13(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.paper = Paper(self.data)

    def solve_part1(self):
        fold_instr = self.paper.fold_instructions[0]
        self.paper.fold(x_fold=fold_instr["x"], y_fold=fold_instr["y"])
        return self.paper.cnt_dots()

    def solve_part2(self):
        for fold_instr in self.paper.fold_instructions[1:]:
            self.paper.fold(x_fold=fold_instr["x"], y_fold=fold_instr["y"])
        print(self.paper)
        return "CJHXZKRU"


def main():
    day = Day13("day13.in")
    day.run()


if __name__ == "__main__":
    main()
