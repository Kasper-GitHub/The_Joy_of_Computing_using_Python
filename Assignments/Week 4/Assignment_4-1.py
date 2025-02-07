order = int(input())
matrix = []

for i in range(order):
    row = input().split(" ")
    for j in range(order):
        row[j] = int(row[j])
    matrix.append(row)

def isDiagonalMatrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if (i != j) and (mat[i][j] != 0):
                return 0
    return 1

result = isDiagonalMatrix(matrix)
print(result, end="")