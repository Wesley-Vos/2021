import unittest

from aoc.days.day12 import Day12


class Day12Test(unittest.TestCase):
    example_day = Day12("../input/test/day12.in")
    real_day = Day12("../input/day12.in")

    def test_example_1(self):
        example_answer1 = 10
        self.assertEqual(self.example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 36
        self.assertEqual(self.example_day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 3563
        self.assertEqual(self.real_day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 105453
        self.assertEqual(self.real_day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
