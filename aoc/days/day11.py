from aoc.util.Day import Day


class Octopuses:
    class Octopus:
        def __init__(self, pos, energy):
            self.energy = int(energy)
            self.x, self.y = pos
            self.neighbours = [(self.x + dx, self.y + dy) for dx, dy in {(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)}]
        
        def step(self):
            self.energy += 1
        
        def can_flash(self):
            return self.energy > 9
            
        def flash(self):
            self.energy = 0 if self.can_flash() else self.energy
    
    def __init__(self, data):
        self.grid = {}
        self.steps = 0
        self.size_x, self.size_y = len(data[0]), len(data)
        self.grid = {(x, y): self.Octopus((x, y), energy) for y, row in enumerate(data) for x, energy in enumerate(row)}

    def __str__(self):
        out = ""
        for y in range(self.size_y):
            out += (" ".join(str(self.grid.get((x,y)).energy) for x in range(self.size_x))) + "\n"
        return out

    def _step(self):
        self.steps += 1
        for pos, octo in self.grid.items():
            octo.step()
        
        to_check = {(x, y): octo for (x, y), octo in self.grid.items() if octo.can_flash()}
        to_flash = []

        while len(to_check):
            for (x, y), octo in to_check.copy().items():
                to_check.pop((x, y))
                to_flash.append((x, y))
                for neighbour in octo.neighbours:
                    if neighbour in self.grid:
                        octo = self.grid.get(neighbour)
                        octo.step()
                        if octo.can_flash() and neighbour not in to_flash:
                            to_check[neighbour] = octo

        cnt = len(to_flash)
        for octo in map(self.grid.get, to_flash):
            octo.flash()
        
        return cnt

    def cnt_flashes(self, steps):
        return sum(self._step() for _ in range(steps))

    def sim_flash(self):
        while self._step() != (self.size_x * self.size_y):
            pass
        return self.steps
 

class Day11(Day):
    def __init__(self, filename):
        super().__init__(filename)
    
    def solve_part1(self):
        return Octopuses(self.data).cnt_flashes(100)

    def solve_part2(self):
        return Octopuses(self.data).sim_flash()


def main():
    day = Day11("day11.in")
    day.run()


if __name__ == "__main__":
    main()
