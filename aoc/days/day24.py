from aoc.util.Day import Day

from collections import defaultdict

class MONAD:
    def __init__(self, data):
        self.instructions = [row.split() for row in data]
        self._values = None
        
    def _reset(self):
        self._values = defaultdict(int)
        
    def _process_instruction(self, instruction, digits):
        opt, *val = instruction
        #print(opt, val)
        res = 0
        if opt == "inp":
            res = digits.pop(0)
        else:
            a = self._values[val[0]]
            b = int(val[1]) if val[1].isdigit() else self._values[val[1]]

            match opt:
                case "add": res = a + b
                case "mul": res = a * b
                case "div": res = int(a/b)
                case "mod": res = a%b
                case "eql": res = int(a == b)
                    
        self._values[val[0]] = res
    
    def validate_model_number(self, modelnumber):
        print(f"Validate {modelnumber}")
        if '0' in str(modelnumber):
            return False
        self._reset()
        digits = list(map(int, str(modelnumber)))
        
        for i, instruction in enumerate(self.instructions):
            self._process_instruction(instruction, digits)
        
        return self._values['z'] == 0
        
        
class Day24(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.MONAD = MONAD(self.data)

    def solve_part1(self):
        modelnumber = 99999999999999
        while modelnumber > 0:
            if self.MONAD.validate_model_number(modelnumber):
                return modelnumber
            modelnumber -= 1
        return 0

    def solve_part2(self):
        return None


def main():
    day = Day24("test/day24.in")
    day.run()


if __name__ == "__main__":
    main()
