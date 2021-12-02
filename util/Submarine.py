class Submarine:

    class Position:
        def __init__(self):
            self.x = 0
            self.depth = 0
            self.aim = 0

    position = None

    FORWARD = "forward"
    UP = "up"
    DOWN = "down"

    def __init__(self):
        self.position = self.Position()
        self.directions = {
            self.FORWARD: self._forward,
            self.UP: self._up,
            self.DOWN: self._down
        }

    def _forward(self, amount, part):
        self.position.x += amount
        if part == 2:
            self.position.depth += amount*self.position.aim

    def _down(self, amount, part):
        if part == 1:
            self.position.depth += amount
        elif part == 2:
            self.position.aim += amount

    def _up(self, amount, part):
        if part == 1:
            self.position.depth -= amount
        elif part == 2:
            self.position.aim -= amount

    def move(self, direction, amount, part=1):
        if direction in self.directions:
            self.directions.get(direction)(amount, part)
