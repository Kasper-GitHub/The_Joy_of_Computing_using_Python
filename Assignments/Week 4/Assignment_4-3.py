order = int(input())
matrix = []

for i in range(order):
    row = input().split(" ")
    for j in range(order):
        row[j] = int(row[j])
    matrix.append(row)

def isSymmetricMatrix(mat):
    n = len(mat)
    mat_T = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
      for j in range(n):
        mat_T[j][i] = mat[i][j]

    for i in range(n):
        for j in range(n):
            if mat_T[i][j] != mat[i][j]:
                return 0
    return 1

result = isSymmetricMatrix(matrix)
print(result, end="")