import unittest

from aoc.days.day7 import Day7


class Day3Test(unittest.TestCase):
    def test_example_1(self):
        example_answer1 = 37
        day = Day7("../input/test/day7.in")
        self.assertEqual(day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 168
        day = Day7("../input/test/day7.in")
        self.assertEqual(day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 352707
        day = Day7("../input/day7.in")
        self.assertEqual(day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 95519693
        day = Day7("../input/day7.in")
        self.assertEqual(day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
