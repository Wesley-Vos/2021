from aoc.util.Day import Day

import re


class Shoot:
    def __init__(self, data):
        self.x1, self.x2, self.y1, self.y2 = map(int, re.findall(r"-?\d+", data))
        self.max_y = 0
    
    def _sim(self, vx, vy, px, py):
        px += vx
        py += vy
        vx -= (vx > 0)
        vy -= 1
        if py < self.y1 or px > self.x2:
            return 0
        if self.y2 >= py and self.x1 <= px:
            return 1
        return self._sim(vx, vy, px, py)
        
        
    def sim_all(self):
        hits = set()
        for vx in range(1, 1+self.x2):
            for vy in range(self.y1, -self.y1):
                # print(f"Try {vx}, {vy}")
                if self._sim(vx, vy, 0, 0):
                    hits.add((vx, vy))
        return len(hits)
        
    def get_max_y(self):
        return self.y1*(self.y1 + 1)//2
        

class Day17(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.shoot = Shoot(self.data[0])

    def solve_part1(self):
        return self.shoot.get_max_y()

    def solve_part2(self):
        return self.shoot.sim_all()


def main():
    day = Day17("day17.in")
    day.run()


if __name__ == "__main__":
    main()
