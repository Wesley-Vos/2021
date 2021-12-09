from aoc.util.Day import Day
from itertools import permutations


class SevenSegmentSearch:
    def __init__(self, data):
        self.data = [list(map(str.split, d.split("|"))) for d in data]
        self.output = [d.split("|")[1].split() for d in data]

    def cnt_unique(self):
        return len([d for d in [d for row in self.output for d in row] if len(d) in (2, 3, 4, 7)])

    @staticmethod
    def _decode(output):
        signal = output[0]
        digits = output[1]

        config = {
            "T": None,
            "M": None,
            "B": None,
            "LT": None,
            "RT": None,
            "LB": None,
            "RB": None
        }

        map_pattern = {}

        for pattern in signal:
            match len(pattern):
                case 2: map_pattern[1] = pattern
                case 3: map_pattern[7] = pattern
                case 4: map_pattern[4] = pattern
                case 7: map_pattern[8] = pattern

        config["T"] = list(set(map_pattern.get(7)).difference(set(map_pattern.get(1))))[0]

        len_pattern = [[] for i in range(0, 8)]
        for pattern in signal:
            len_pattern[len(pattern)].append(pattern)

        common = set(len_pattern[5][0]).intersection(set(len_pattern[5][1])).intersection(set(len_pattern[5][2]))
        m_b = common.difference(set(config["T"]))

        config['M'] = list(set(map_pattern.get(4)).difference(set(map_pattern.get(1))).intersection(m_b))[0]
        config['B'] = list(m_b.difference(set(config['M'])))[0]
        config['LT'] = list(set(map_pattern.get(4)).difference(set(map_pattern.get(1))).difference(set(config['M'])))[0]
        config['LB'] = list(set(map_pattern.get(8)).difference(set(map_pattern.get(4))).difference({config['T'], config['B']}))[0]

        new_mapping = {}

        for pattern in len_pattern[5]:
            if config['LT'] in pattern:
                new_mapping[5] = pattern
            elif config['LB'] in pattern:
                new_mapping[2] = pattern
            else:
                new_mapping[3] = pattern

        new_mapping[0] = ''.join(set(map_pattern[8]).difference(config['M']))
        config['RB'] = list(set(new_mapping[0]).difference({config['T'], config['B'], config['LB'], config['LT']}))[0]

        for pattern in len_pattern[6]:
            if pattern not in [''.join(list(perm)) for perm in permutations(new_mapping[0])]:
                if config['LB'] in pattern and config['LT'] in pattern:
                    new_mapping[6] = pattern
                else:
                    new_mapping[9] = pattern

        new_mapping[1] = map_pattern[1]
        new_mapping[4] = map_pattern[4]
        new_mapping[7] = map_pattern[7]
        new_mapping[8] = map_pattern[8]

        digit_mapping = {mapping: key for key, mapping in new_mapping.items()}

        for key, mapping in dict(digit_mapping.items()).items():
            for perm in permutations(key):
                digit_mapping[''.join(list(perm))] = mapping

        return sum((int(digit_mapping[digit]) * pow(10, i)) for i, digit in enumerate(reversed(digits)))

    def summed_decode(self):
        return sum(map(self._decode, self.data))


class Day8(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.sss = SevenSegmentSearch(self.data)

    def solve_part1(self):
        return self.sss.cnt_unique()

    def solve_part2(self):
        return self.sss.summed_decode()


def main():
    day = Day8("day8.in")
    day.run()


if __name__ == "__main__":
    main()
