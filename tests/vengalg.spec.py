import unittest

from main.vengalg import VengAlg


class Test(unittest.TestCase):

    def setUp(self):
        self.matrix = [[7, 7, 3, 6],
                       [4, 9, 5, 4],
                       [5, 5, 4, 5],
                       [6, 4, 7, 2]]

    def test_is_not_covered_cols_present(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        veng = VengAlg(matrix)
        self.assertEqual(veng.is_not_covered_cols_present(), True)
        matrix[1][1] = 0
        matrix[2][2] = 0
        matrix[0][0] = 0
        self.assertEqual(veng.is_not_covered_cols_present(), False)

    def test_apply_for_col(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        veng = VengAlg(matrix)
        self.assertEqual(veng.apply_for_col(0, lambda array: [item * 2 for item in array]), [2, 8, 14])

    def test_get_uncovered_cols_indexes(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        veng = VengAlg(matrix)
        self.assertEqual(veng.get_not_covered_col_indexes(), [0, 1, 2])
        matrix = [[2, 0],
                  [1, 0]]
        veng = VengAlg(matrix)
        self.assertEqual(veng.get_not_covered_col_indexes(), [0])

    def test_reduce_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        veng = VengAlg(matrix)
        veng.reduce_matrix(min)
        self.assertEqual(veng.matrix, [[0, 0, 0],
                                       [0, 0, 0],
                                       [0, 0, 0]])
        matrix = [[1, 1, 1],
                  [4, 5, 6],
                  [7, 8, 9]]
        veng = VengAlg(matrix)
        veng.reduce_matrix(min)
        self.assertEqual(veng.matrix, [[0, 0, 0],
                                       [0, 1, 2],
                                       [0, 1, 2]])

    def test_build_adjacency_matrix(self):
        matrix = [[15, 0, 23], [0, 7, -10], [0, 4, 5]]
        veng = VengAlg(matrix)
        self.assertEqual(veng.build_adjacency_matrix(), [[False, True, False],
                                                         [True, False, False],
                                                         [True, False, False]])

    def test_get_max_matchings(self):
        matrix = [[15, 0, 23], [0, 7, -10], [0, 4, 5]]
        veng = VengAlg(matrix)
        matrix = veng.build_adjacency_matrix()
        self.assertEqual(veng.get_max_matchings(matrix), [(1, 0), (0, 1)])
        self.assertEqual(veng.is_perfect_matchings(veng.get_max_matchings(matrix)), False)
        matrix = [[1, 0, 23], [0, 1, -10], [0, 4, 0]]
        veng = VengAlg(matrix)
        matrix = veng.build_adjacency_matrix()
        self.assertEqual(veng.get_max_matchings(matrix), [(1, 0), (0, 1), (2, 2)])
        self.assertEqual(veng.is_perfect_matchings(veng.get_max_matchings(matrix)), True)

    def test_get_free_vertex(self):
        matrix = [[28, 24, 0, 22, 0],
                  [13, 15, 0, 13, 0],
                  [0, 0, 1, 0, 0],
                  [13, 10, 0, 10, 0],
                  [17, 12, 0, 9, 0]]
        veng = VengAlg(matrix)
        matrix = veng.build_adjacency_matrix()
        max_matchings = veng.get_max_matchings(matrix)
        self.assertEqual(max_matchings, [(2, 0), (1, 2), (0, 4)])
        self.assertEqual(veng.get_free_vertex(max_matchings), {'rows': [3, 4], 'cols': [1, 3]})

    def test_execute(self):
         matrix = [[32, 28, 4, 26, 4],
                  [17, 19, 4, 17, 4],
                  [4, 4, 1, 4, 4],
                  [17, 14, 4, 14, 4],
                  [21, 16, 4, 13, 4]]
         veng = VengAlg(matrix)
         self.assertEqual(veng.execute(), [(2, 0), (3, 1), (1, 2), (4, 3), (0, 4)])




