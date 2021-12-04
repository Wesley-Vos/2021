def max_tied(a, b, tie):
    return tie if a == b else (a if tie else b)


class Submarine:
    class Diagnostics:
        def __init__(self, report):
            self.report = report

        @staticmethod
        def _get_commons(report):
            report = zip(*map(list, report))
            report = list(map(lambda r: tuple(map(int, r)), report))
            most_common = [max(set(bit), key=bit.count) for bit in report]
            least_common = [min(set(bit), key=bit.count) for bit in report]
            return most_common, least_common

        @staticmethod
        def _bitstring_to_int(bitstring):
            return int(''.join(map(str, bitstring)), 2)

        def _filter_report(self, most):
            filtered_report = [list(map(int, bit)) for bit in self.report]

            idx = 0
            while len(filtered_report) > 1:
                #print("Before filter", filtered_report)
                most_common, least_common = self._get_commons(filtered_report)
                check = max_tied(most_common[idx], least_common[idx], int(most))
                #print(check)
                filtered_report = [bit for bit in filtered_report if bit[idx] == check]
                #print("After filter", filtered_report)
                idx += 1
            return filtered_report[0]

        def analyse_power(self):
            most_common, least_common = self._get_commons(self.report)

            gamma = self._bitstring_to_int(most_common)
            terra = self._bitstring_to_int(least_common)
            return gamma, terra

        def analyse_living(self):
            filter_most = self._filter_report(True)
            filter_least = self._filter_report(False)

            oxygen = self._bitstring_to_int(filter_most)
            co2 = self._bitstring_to_int(filter_least)
            return oxygen, co2

    class Position:
        def __init__(self):
            self.x = 0
            self.depth = 0

    position = None

    def __init__(self):
        self.position = self.Position()

    def _forward(self, amount):
        self.position.x += amount

    def _down(self, amount):
        self.position.depth += amount

    def _up(self, amount):
        self.position.depth -= amount

    def move(self, direction, amount):
        eval(f'self._{direction}({amount})')

    def calculate_power_consumption(self, report):
        diagnostics = self.Diagnostics(report)
        gamma, terra = diagnostics.analyse_power()
        return gamma * terra

    def calculate_life_support_rating(self, report):
        diagnostics = self.Diagnostics(report)
        oxygen, co2 = diagnostics.analyse_living()
        return oxygen * co2


class AimedSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def _forward(self, amount):
        super()._forward(amount)
        self.position.depth += amount * self.aim

    def _down(self, amount):
        self.aim += amount

    def _up(self, amount):
        self.aim -= amount
