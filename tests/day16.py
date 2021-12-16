import unittest

from aoc.days.day16 import Day16


class Day16Test(unittest.TestCase):
    example_day = Day16("../input/test/day16-1.in")
    real_day = Day16("../input/day16.in")

    def test_example_1_1(self):
        example_day = Day16("../input/test/day16-1.in")
        example_answer1 = 16
        self.assertEqual(example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_1_2(self):
        example_day = Day16("../input/test/day16-2.in")
        example_answer1 = 12
        self.assertEqual(example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_1_3(self):
        example_day = Day16("../input/test/day16-3.in")
        example_answer1 = 23
        self.assertEqual(example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_1_4(self):
        example_day = Day16("../input/test/day16-4.in")
        example_answer1 = 31
        self.assertEqual(example_day.solve_part1(), example_answer1, f"The example test for part 1 should return {example_answer1}")

    def test_example_2(self):
        example_answer2 = 0
        self.assertEqual(self.example_day.solve_part2(), example_answer2, f"The example test for part 2 should return {example_answer2}")

    def test_part1(self):
        answer1 = 3406
        self.assertEqual(self.real_day.solve_part1(), answer1, f"The test for part 1 should return {answer1}")

    def test_part2(self):
        answer2 = 3941782230241
        self.assertEqual(self.real_day.solve_part2(), answer2, f"The test for part 2 should return {answer2}")


if __name__ == '__main__':
    unittest.main()
