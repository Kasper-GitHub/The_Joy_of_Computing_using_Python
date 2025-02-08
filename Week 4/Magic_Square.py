import numpy as np

def coordinate_adjust(p,q,n):
    if p == -1 and q == n:
        p = 0
        q = n - 2
    else:
        if p == -1:
            p = n - 1
        elif q == n:
            q = 0
    return p,q

n = int(input("Enter the size of Magic Square : "))
magic_square = np.zeros((n, n))
value = 1
p = n//2
q = n-1

magic_square[p][q] = value
value += 1

while value <= n**2:
    p -= 1
    q += 1

    adjust = coordinate_adjust(p, q, n)
    p = adjust[0]
    q = adjust[1]

    if magic_square[p][q] == 0:
        magic_square[p][q] = value
    else:
        while magic_square[p][q] != 0:
            p += 1
            q -= 2

            adjust = coordinate_adjust(p,q,n)
            p = adjust[0]
            q = adjust[1]

        magic_square[p][q] = value

    value += 1

print("Magic Square of order ",n," is ")
print(np.matrix(magic_square))
print("Sum of terms column-wise : ",np.sum(magic_square, axis = 0, dtype = int))
print("Sum of terms row-wise : ",np.sum(magic_square, axis = 1, dtype = int))
print("Sum of terms diagonal-wise : ", np.trace(magic_square, offset=0, axis1=0, axis2=1, dtype = int),np.trace(magic_square, offset=0, axis1=1, axis2=0, dtype = int))