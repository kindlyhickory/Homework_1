import numpy as np


class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return str('\n'.join(['  '.join([str(j) for j in i]) for i in self.matr]))

    def __add__(self, other):
        sum_matr = np.ones(np.shape(self.matr))
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                sum_matr[i][j] = self.matr[i][j] + other.matr[i][j]
        return str('\n'.join(['  '.join([str(j) for j in i]) for i in sum_matr]))


my_matr_1 = Matrix([[1, 2, 3, 5],
                    [4, 9, 6, 7],
                    [8, 1, 4, 7]
                    ])
my_matr_2 = Matrix([[3, 4, 5, 5],
                    [2, 1, 4, 3],
                    [2, 9, 6, 3]
                    ])
print(my_matr_1 + my_matr_2)
