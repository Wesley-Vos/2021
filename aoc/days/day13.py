import re

from aoc.util.Day import Day


class Paper:
    def __init__(self, data):
        self.grid = {}
        self.size = {"x": 0, "y": 0}
        self.fold_instructions = []
        for x, y in data:
            self.size["x"] = max(self.size["x"], x + 1)
            self.size["y"] = max(self.size["y"], y + 1)
            self.grid[(x, y)] = 1

    def __str__(self):
        return "\n".join("".join("██" if (x, y) in self.grid else "  " for x in range(self.size['x'])) for y in
                         range(self.size['y']))

    def mirror(self, des, src):
        if src in self.grid or des in self.grid:
            self.grid[des] = 1

    def remove(self, pos):
        self.grid.pop(pos, None)

    def cnt_dots(self):
        return len(self.grid.values())


class PaperFolder:
    def __init__(self, paper, instructions):
        self.paper = paper
        self.instructions = instructions

    def fold_all(self):
        while len(self.instructions) > 0:
            self.fold()

    def fold(self):
        self._process_instruction(self.instructions.pop(0))

    def _process_instruction(self, instruction):
        x_fold, y_fold = instruction
        dx, dy = ((x_fold or -1) + 1), ((y_fold or -1) + 1)
        size = {'x': x_fold or self.paper.size['x'], 'y': y_fold or self.paper.size['y']}

        for x in range(dx, self.paper.size['x']):
            for y in range(dy, self.paper.size['y']):
                mirrored = (2 * x_fold - x, y) if x_fold is not None else (x, 2 * y_fold - y)
                self.paper.mirror(mirrored, (x, y))
                self.paper.remove((x, y))

        self.paper.size = size


class Day13(Day):
    def __init__(self, filename):
        super().__init__(filename)
        grid, instructions = self._split_input()
        self.paper = Paper(grid)
        self.folder = PaperFolder(self.paper, instructions)

    def _split_input(self):
        grid, instructions = [], []

        for row in filter(lambda r: r != "", self.data):
            if row[0].isnumeric():
                grid.append(tuple(map(int, row.split(","))))
            else:
                reg_pattern = r"fold along ([xy])=(\d*)"
                xy, val = re.findall(reg_pattern, row, re.MULTILINE)[0]
                instructions.append((int(val) if xy == 'x' else None, int(val) if xy == 'y' else None))

        return grid, instructions

    def solve_part1(self):
        self.folder.fold()
        return self.paper.cnt_dots()

    def solve_part2(self):
        self.folder.fold_all()
        return "\n" + str(self.paper)


def main():
    day = Day13("day13.in")
    day.run()


if __name__ == "__main__":
    main()
