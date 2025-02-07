order_row = int(input())
order_col = int(input())

matrix = []
matrix_T = [[0 for i in range(order_row)] for j in range(order_col)]

for i in range(order_row):
    row = input().split(" ")
    for j in range(order_col):
        row[j] = int(row[j])
    matrix.append(row)

scalar = int(input())

for i in range(order_row):
    for j in range(order_col):
        matrix_T[j][i] = matrix[i][j]
        matrix_T[j][i] = matrix_T[j][i]  + scalar

for i in range(order_col-1):
    print(' '.join(map(str,matrix_T[i])))
print(' '.join(map(str,matrix_T[order_col-1])), end='')