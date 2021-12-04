import unittest

from aoc.days.day2 import Day2


class Day2Test(unittest.TestCase):
    def test_example_1(self):
        example_answer1 = 150
        day2 = Day2("test/day2.txt")
        self.assertEqual(day2.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 900
        day2 = Day2("test/day2.txt")
        self.assertEqual(day2.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 1654760
        day2 = Day2("day2.txt")
        self.assertEqual(day2.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 1956047400
        day2 = Day2("day2.txt")
        self.assertEqual(day2.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
