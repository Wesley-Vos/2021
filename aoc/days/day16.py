from aoc.util.Day import Day
import sys

sys.setrecursionlimit(50)

class PacketDecoder:
    def __init__(self, data):
        bin_string = self._hex_to_bin(data[0])
        self.packet, _ = self._parse(bin_string)

    @staticmethod
    def _hex_to_bin(string):
        return bin(int(string, 16))[2:].zfill(len(string) * 4)

    def _parse(self, packet):
        print(packet)
        version = int(packet[0:3], 2)
        type_ID = int(packet[3:6], 2)
        print(f"Version: {version} and type: {type_ID}")
        i = 6
        new_packet = None
        if type_ID == 4:
            cont = True
            bit_string = ""
            while cont:
                start = int(packet[i], 2)
                i += 1
                cont = bool(start)
                bit_string = bit_string + packet[i:i + 4]
                i += 4
            value = int(bit_string, 2)
            new_packet = Literal(version, type_ID, value)

        else:
            self.length_type_ID = int(packet[i], 2)
            i += 1
            if self.length_type_ID == 0:
                length_subpackets = int(packet[i:i + 15], 2)
                print(f"Length mode, {length_subpackets}")
                i += 15
                while i < i + length_subpackets:
                    pass

                # total length of subpackets = 15
            else:
                numb_subpackets = int(packet[i:i + 11], 2)
                print(f"Number mode {numb_subpackets}")
                for i in range(numb_subpackets):
                    print(f"Send {packet[i:]}")
                    new_packet, rest = self._parse(packet[i:])
                    print(f"Got: {new_packet} with rest {rest}")


        return new_packet, packet[i:]


class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id


class Literal(Packet):
    def __init__(self, version, type_id, value):
        super().__init__(version, type_id)
        self.value = value

    def __str__(self):
        return f"Literal with version {self.version}, type_ID {self.type_id} and value {self.value}"


class Operator(Packet):
    def __init__(self, version, type_id):
        super().__init__(version, type_id)


class Day16(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.packet_decoder = PacketDecoder(self.data)
        print(self.packet_decoder.packet)

    def solve_part1(self):
        return None

    def solve_part2(self):
        return None


def main():
    day = Day16("test/day16-0.in")
    day.run()


if __name__ == "__main__":
    main()
