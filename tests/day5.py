import unittest

from aoc.days.day5 import Day5


class Day3Test(unittest.TestCase):
    def test_example_1(self):
        example_answer1 = 5
        day = Day5("../input/test/day5.in")
        self.assertEqual(day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 12
        day = Day5("../input/test/day5.in")
        self.assertEqual(day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 6113
        day = Day5("../input/day5.in")
        self.assertEqual(day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 20373
        day = Day5("../input/day5.in")
        self.assertEqual(day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
