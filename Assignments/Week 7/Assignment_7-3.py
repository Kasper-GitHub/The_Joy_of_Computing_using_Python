def rotate_matrix_90_clockwise(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rotated = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            rotated[j][m - 1 - i] = matrix[i][j]

    return rotated


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def main():
    # Read matrix dimensions m x n
    m, n = map(int, input().split())

    # Read the matrix
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))

    # Rotate the matrix
    result = rotate_matrix_90_clockwise(matrix)

    # Print the rotated matrix
    print_matrix(result)


if __name__ == "__main__":
    main()