def find_median(matrix, n, m):
    # Flatten the matrix into a single list
    elements = []
    for row in matrix:
        elements.extend(row)

    # Sort all elements
    elements.sort()

    # Find the median
    median_index = (n * m) // 2
    return elements[median_index]


def main():
    # Read matrix dimensions n x m
    n, m = map(int, input().split())

    # Read the matrix
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # Get and print the median
    print(find_median(matrix, n, m), end='')


if __name__ == "__main__":
    main()
