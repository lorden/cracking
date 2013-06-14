def rotate90(matrix, n):
    for layer in xrange(0, n / 2):
        first = layer
        last = n - 1 - layer
        for i in xrange(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix


def print_matrix(matrix):
    for x in matrix:
        print x

matrix = [
    ['0', '1', '2', '3', '4'],
    ['5', '6', '7', '8', '9'],
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O']
]
n = 5

print_matrix(matrix)
print
print_matrix(rotate90(matrix, n))
