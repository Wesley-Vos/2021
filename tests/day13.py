import unittest

from aoc.days.day13 import Day13


class Day13Test(unittest.TestCase):
    example_day = Day13("../input/test/day13.in")
    real_day = Day13("../input/day13.in")

    def test_example_1(self):
        example_answer1 = 17
        self.assertEqual(self.example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = "\n██████████\n██      ██\n██      ██\n██      ██\n██████████\n          \n          "
        self.assertEqual(self.example_day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 666
        self.assertEqual(self.real_day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = "\n  ████        ████  ██    ██    ████    ████████  ██    ██  ██    ██  ██    ██  \n██    ██        ██  ██    ██  ██    ██        ██  ██    ██  ██  ██    ██    ██  \n██              ██  ████████  ██    ██      ██    ████████  ████      ██    ██  \n██              ██  ██    ██  ████████    ██      ██    ██  ██  ██    ██    ██  \n██    ██  ██    ██  ██    ██  ██    ██  ██        ██    ██  ██  ██    ██    ██  \n  ████      ████    ██    ██  ██    ██  ████████  ██    ██  ██    ██    ████    "
        self.assertEqual(self.real_day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
