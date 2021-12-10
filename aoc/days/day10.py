from aoc.util.Day import Day

class Chunks:
    SYNTAX_SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    PAIRS = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    COMPLETE_SCORES = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def __init__(self, data):
        self.chunks = data
        self.corrupted_closings, self.incomplete = self.process_chunks()

    def process_chunks(self):
        corrupted_closings = []
        incomplete = []
        for chunk in self.chunks:
            opening = []
            for char in chunk:
                if char in self.PAIRS.keys(): # append opening
                    opening.append(char)
                else:
                    opening_char = opening.pop()
                    if char != self.PAIRS.get(opening_char):
                        corrupted_closings.append(char)
                        break
            incomplete.append(opening)
        return corrupted_closings, incomplete

    def sum_corrupted_chunks(self):
        return sum(map(self.SYNTAX_SCORES.get, self.corrupted_closings))

    def sum_incomplete_chunks(self):
        completion_scores = []

        for opening in self.incomplete:
            res = 0
            for char in opening:
                res = res * 5 + self.COMPLETE_SCORES[self.PAIRS.get(char)]
            completion_scores.append(res)

        middle = int(len(completion_scores)/2)
        return sorted(completion_scores)[middle]


class Day10(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.chunks = Chunks(self.data)

    def solve_part1(self):
        return self.chunks.sum_corrupted_chunks()

    def solve_part2(self):
        return self.chunks.sum_incomplete_chunks()


def main():
    day = Day10("test/day10.in")
    day.run()


if __name__ == "__main__":
    main()
