import unittest


class DayTest(unittest.TestCase):
    day_resource = None
    example_file = None
    file = None
    example_1 = None
    example_2 = None
    answer_1 = None
    answer_2 = None

    def test_example_part1(self):
        day = self.day_resource(self.example_file)
        self.assertEqual(day.solve_part1(), self.example_1)

    def test_example_part2(self):
        day = self.day_resource(self.example_file)
        self.assertEqual(day.solve_part2(), self.example_2)

    def test_part1(self):
        day = self.day_resource(self.file)
        self.assertEqual(day.solve_part1(), self.answer_1)

    def test_part2(self):
        day = self.day_resource(self.file)
        self.assertEqual(day.solve_part2(), self.answer_2)
