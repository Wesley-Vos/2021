import unittest

from days.day1 import Day1


class Day2Test(unittest.TestCase):
    def test_example_1(self):
        example_answer1 = 7
        day1 = Day1("test/day1.txt")
        self.assertEqual(day1.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 5
        day1 = Day1("test/day1.txt")
        self.assertEqual(day1.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 1715
        day1 = Day1("day1.txt")
        self.assertEqual(day1.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 1739
        day1 = Day1("day1.txt")
        self.assertEqual(day1.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
