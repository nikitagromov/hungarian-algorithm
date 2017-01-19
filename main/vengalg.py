import sys

from main.kuhn import kuhn


class VengAlg():
    def __init__(self, matrix):
        self.matrix = matrix

    def execute(self):
        self.reduce_matrix(min)
        matchings = self.get_max_matchings(self.build_adjacency_matrix())
        while not self.is_perfect_matchings(matchings):
            free_vertex = self.get_free_vertex(matchings)
            alpha_sets = self.get_sets_for_alpha(matchings, free_vertex)
            self.make_alpha_and_reduce_matrix(alpha_sets)
            matchings = self.get_max_matchings(self.build_adjacency_matrix())
        return matchings

    def reduce_matrix(self, minimize_func):
        for i, row in enumerate(self.matrix):
            reduce_value = minimize_func(row)
            for j, item in enumerate(row):
                self.matrix[i][j] = self.matrix[i][j] - reduce_value
        if self.is_not_covered_cols_present():
            for j in self.get_not_covered_col_indexes():
                reduce_value = self.apply_for_col(j, minimize_func)
                for i in range(len(self.matrix)):
                    self.matrix[i][j] = self.matrix[i][j] - reduce_value

    def build_adjacency_matrix(self):
        return [[item == 0 for item in row] for row in self.matrix]

    def apply_for_col(self, col_index, apply_func):
        reverted_matrix = [[None for item in row] for row in self.matrix]
        for j in range(len(self.matrix)):
            for i in range(len(self.matrix)):
                reverted_matrix[j][i] = self.matrix[i][j]
        return apply_func(reverted_matrix[col_index])

    def is_not_covered_cols_present(self):
        covered_cols = []
        for j in range(len(self.matrix)):
            trigger = False
            for i in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    trigger = True
                    break
            covered_cols.append(trigger)
        for item in covered_cols:
            if not item:
                return True
        return False

    def get_not_covered_col_indexes(self):
        col_indexes = []
        for j in range(len(self.matrix)):
            trigger = False
            for i in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    trigger = True
                    break
            if not trigger:
                col_indexes.append(j)
        return col_indexes

    def get_max_matchings(self, adjacency_matrix):
        matrix = [[1 if x else 0 for x in row] for row in adjacency_matrix]
        result = kuhn(matrix)
        max_matchings = []
        for col, row in enumerate(result):
            if row != -1:
                max_matchings.append((row, col))
        return max_matchings

    def is_perfect_matchings(self, matchings):
        return len(matchings) == len(self.matrix)

    def get_free_vertex(self, max_matchings):
        rows = [0 for i in range(len(self.matrix))]
        cols = [0 for j in rows]
        result = {'rows': [],
                  'cols': []}

        for item in max_matchings:
            i, j = item
            rows[i] = 1
            cols[j] = 1

        for i in range(len(rows)):
            if rows[i] == 0:
                result['rows'].append(i)
            if cols[i] == 0:
                result['cols'].append(i)
        return result

    def get_sets_for_alpha(self, max_matchings, free_vertexes):
        vertexes = []
        chain = set()
        for i in free_vertexes['rows']:
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    vertexes.append((i, j))
        for vertex in vertexes:
            i, j = vertex
            for item in max_matchings:
                ii, jj = item
                if j == jj:
                    chain.add((ii, jj))
        x = set()
        y = set()
        yy = set()
        for item in chain:
            i, j = item
            x.add(i)
            y.add(j)
        for item in free_vertexes['rows']:
            x.add(item)
        for i in range(len(self.matrix)):
            yy.add(i)

        return {'rows': x, 'cols': yy - y}

    def make_alpha_and_reduce_matrix(self, sets):
        xlist = list(sets['rows'])
        ylist = list(sets['cols'])
        res = [[-1 for item in row] for row in self.matrix]
        for i in xlist:
            for j in ylist:
                res[i][j] = self.matrix[i][j]
        minimum = sys.maxsize

        for i, row in enumerate(res):
            for j in range(len(res)):
                if minimum > res[i][j] and res[i][j] != -1 and res[i][j] != 0:
                    minimum = res[i][j]
        cols = set([i for i in range(len(self.matrix))]) - sets['cols']
        for i in xlist:
            for j in range(len(self.matrix)):
                self.matrix[i][j] -= minimum
        for i in range(len(self.matrix)):
            for j in list(cols):
                self.matrix[i][j] += minimum
