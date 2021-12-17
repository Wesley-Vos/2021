from aoc.util.Day import Day
from math import prod


class PacketDecoder:
    def __init__(self, data):
        bin_string = self._hex_to_bin(data[0])
        self.packet, _ = self._parse(bin_string)

    @staticmethod
    def _hex_to_bin(string):
        return bin(int(string, 16))[2:].zfill(len(string) * 4)

    def _parse(self, packet):
        version = int(packet[0:3], 2)
        type_ID = int(packet[3:6], 2)
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
            length_type_ID = int(packet[i], 2)
            subs = []
            i += 1
            if length_type_ID == 0:
                length_subpackets = int(packet[i:i + 15], 2)
                i += 15
                len_after = len(packet[i:]) - length_subpackets
                while len(packet) > len_after:
                    new_packet, packet = self._parse(packet[i:])
                    subs.append(new_packet)
                    i = 0
            else:
                numb_subpackets = int(packet[i:i + 11], 2)
                i += 11
                for j in range(numb_subpackets):
                    new_packet, packet = self._parse(packet[i:])
                    subs.append(new_packet)
                    i = 0
            new_packet = Operator(version, type_ID, length_type_ID, subs)

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

    def version_val(self):
        return self.version
        
    def val(self):
        return self.value


class Operator(Packet):
    def __init__(self, version, type_id, length_type_ID, subpackets):
        super().__init__(version, type_id)
        self.length_type_ID = length_type_ID
        self.subpackets = subpackets
        
    def version_val(self):
        return sum(sub.version_val() for sub in self.subpackets) + self.version
        
    def val(self):
        match self.type_id:
            case 0: return sum(sub.val() for sub in self.subpackets)
            case 1: return prod(sub.val() for sub in self.subpackets)
            case 2: return min(sub.val() for sub in self.subpackets)
            case 3: return max(sub.val() for sub in self.subpackets)
            case 5: return self.subpackets[0].val().__gt__(self.subpackets[1].val())
            case 6: return self.subpackets[0].val().__lt__(self.subpackets[1].val())
            case 7: return self.subpackets[0].val().__eq__(self.subpackets[1].val())

    def __str__(self):
        return f"Operator with version {self.version}, type_ID {self.type_id} and {len(self.subpackets)} subpackets"


class Day16(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.packet = PacketDecoder(self.data).packet
        print(self.packet)

    def solve_part1(self):
        return self.packet.version_val()

    def solve_part2(self):
        return self.packet.val()


def main():
    day = Day16("day16.in")
    day.run()


if __name__ == "__main__":
    main()
