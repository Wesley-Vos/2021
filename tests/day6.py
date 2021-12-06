import unittest

from aoc.days.day6 import Day6


class Day3Test(unittest.TestCase):
    def test_example_1(self):
        example_answer1 = 5934
        day = Day6("../input/test/day6.in")
        self.assertEqual(day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 26984457539
        day = Day6("../input/test/day6.in")
        self.assertEqual(day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 374927
        day = Day6("../input/day6.in")
        self.assertEqual(day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 1687617803407
        day = Day6("../input/day6.in")
        self.assertEqual(day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
