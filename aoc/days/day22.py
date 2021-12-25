from aoc.util.Day import Day

import re

RE_PATTERN = r"^(on|off) x=(-?\d*)..(-?\d*),y=(-?\d*)..(-?\d*),z=(-?\d*)..(-?\d*)$"


class ReactorGrid:
    def __init__(self, data):
        self.on = set()
        for row in data:
            res = re.findall(RE_PATTERN, row, re.MULTILINE)[0]
            state = res[0] == "on"
            x1, x2, y1, y2, z1, z2 = map(int, res[1:])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        if state:
                            self.on.add((x,y,z))
                        else:
                            self.on.discard((x, y, z))
    
    def cnt(self):
        return len(self.on)

class Day22(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.grid = ReactorGrid(self.data)

    def solve_part1(self):
        return self.grid.cnt()

    def solve_part2(self):
        return None


def main():
    day = Day22("test/day22.in")
    day.run()


if __name__ == "__main__":
    main()
