import unittest

from aoc.days.day14 import Day14


class Day14Test(unittest.TestCase):
    example_day = Day14("../input/test/day14.in")
    real_day = Day14("../input/day14.in")

    def test_example_1(self):
        example_answer1 = 1588
        self.assertEqual(self.example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 2188189693529
        self.assertEqual(self.example_day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 3406
        self.assertEqual(self.real_day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 3941782230241
        self.assertEqual(self.real_day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
