import unittest

from aoc.days.day9 import Day9


class Day9Test(unittest.TestCase):
    def test_example_1(self):
        example_answer1 = 15
        day = Day9("../input/test/day9.in")
        self.assertEqual(day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 1134
        day = Day9("../input/test/day9.in")
        self.assertEqual(day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 448
        day = Day9("../input/day9.in")
        self.assertEqual(day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 95519693
        day = Day9("../input/day9.in")
        self.assertEqual(day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
