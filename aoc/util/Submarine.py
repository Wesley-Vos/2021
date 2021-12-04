class Submarine:
    class Diagnostics:
        def __init__(self, report):
            self.report = report

        @staticmethod
        def max_tied(a, b, tie):
            return tie if a == b else (a if tie else b)

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
                # print("Before filter", filtered_report)
                most_common, least_common = self._get_commons(filtered_report)
                check = self.max_tied(most_common[idx], least_common[idx], int(most))
                # print(check)
                filtered_report = [bit for bit in filtered_report if bit[idx] == check]
                # print("After filter", filtered_report)
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
    diagnostics = None

    def __init__(self):
        self.position = self.Position()

    def move(self, direction, amount):
        match direction:
            case "forward":
                self.position.x += amount
            case "up":
                self.position.depth -= amount
            case "down":
                self.position.depth += amount

    def insert_diagnostics_report(self, report):
        self.diagnostics = self.Diagnostics(report)

    def calculate_power_consumption(self):
        gamma, terra = self.diagnostics.analyse_power()
        return gamma * terra

    def calculate_life_support_rating(self):
        oxygen, co2 = self.diagnostics.analyse_living()
        return oxygen * co2


class AimedSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move(self, direction, amount):
        match direction:
            case "forward":
                self.position.x += amount
                self.position.depth += amount * self.aim
            case "up":
                self.aim -= amount
            case "down":
                self.aim += amount
