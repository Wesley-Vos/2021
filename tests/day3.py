import unittest

from days.day3 import Day3


class Day3Test(unittest.TestCase):
    def test_example_1(self):
        example_answer1 = 198
        day = Day3("test/day3.txt")
        self.assertEqual(day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 230
        day = Day3("test/day3.txt")
        self.assertEqual(day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 2498354
        day = Day3("day3.txt")
        self.assertEqual(day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 3277956
        day = Day3("day3.txt")
        self.assertEqual(day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
