import unittest

from main.kuhn import kuhn


class TestCase(unittest.TestCase):

    def test_kuhn(self):
        matrix = [[1, 0, 0], [0, 0, 0], [0, 1, 1]]
        self.assertEqual(kuhn(matrix), [0, 2, -1])
        matrix = [[0, 0], [0, 0]]
        self.assertEqual(kuhn(matrix), [-1, -1])
        matrix = [[1, 0], [0, 0]]
        self.assertEqual(kuhn(matrix), [0, -1])
        matrix = [[1, 1, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEqual(kuhn(matrix), [0, 2, 1])
