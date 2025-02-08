import numpy as np
# Driver Code
magic_square_chk = [[1, 14, 4, 15],
       [8, 11, 5, 10],
       [13, 2, 16, 3],
       [12, 7, 9, 6]]

n = len(magic_square_chk)

col_sum = np.sum(magic_square_chk, axis = 0, dtype = int)
row_sum = np.sum(magic_square_chk, axis = 1, dtype = int)
diag_sum1 = np.trace(magic_square_chk, offset=0, axis1=0, axis2=1, dtype = int)
diag_sum2 = np.trace(magic_square_chk, offset=0, axis1=1, axis2=0, dtype = int)
diag_sum = np.array([diag_sum1,diag_sum2])

print(np.matrix(magic_square_chk))

if np.sum(row_sum)/n == np.sum(diag_sum)/2 and np.sum(col_sum)/n == np.sum(diag_sum)/2:
    print("Given Matrix is Magic Square")
else:
    print("Given Matrix is not Magic Square")