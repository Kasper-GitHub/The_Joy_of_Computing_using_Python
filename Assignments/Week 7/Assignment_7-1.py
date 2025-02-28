import numpy as np

def is_magic_square(matrix, n):
    numpy_matrix = np.array(matrix)
    n = len(numpy_matrix)

    col_sum = np.sum(numpy_matrix, axis=0, dtype=int)
    row_sum = np.sum(numpy_matrix, axis=1, dtype=int)
    diag_sum1 = np.trace(numpy_matrix, offset=0, axis1=0, axis2=1, dtype=int)
    diag_sum2 = np.trace(numpy_matrix, offset=0, axis1=1, axis2=0, dtype=int)
    diag_sum = np.array([diag_sum1, diag_sum2])

    if np.sum(row_sum) / n == np.sum(diag_sum) / 2 and np.sum(col_sum) / n == np.sum(diag_sum) / 2:
        return "Magic Matrix"
    else:
        return "Not a Magic Matrix"

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(is_magic_square(matrix, n))