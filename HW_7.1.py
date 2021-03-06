class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        m = self.matrix
        return "\n".join(map(lambda x: '   '.join(map(str, x)), m))

    def __add__(self, other):
        return Matrix(map(lambda m1, m2: map(lambda x, y: x + y, m1, m2), self.matrix, other.matrix))


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
