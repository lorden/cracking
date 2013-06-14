def zerofy(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zero_rows = [1] * m
    zero_cols = [1] * n

    for x in xrange(0, m):
        for y in xrange(0, n):
            if matrix[x][y] == 0:
                zero_rows[x] = 0
                zero_cols[y] = 0

    for x in xrange(0, m):
        for y in xrange(0, n):
            if zero_rows[x] == 0 or zero_cols[y] == 0:
                matrix[x][y] = 0

    return matrix


def print_matrix(matrix):
    for x in matrix:
        print x

matrix = [
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
print_matrix(matrix)
print
print_matrix(zerofy(matrix))
