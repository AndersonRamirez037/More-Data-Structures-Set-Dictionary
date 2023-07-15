def square_matrix_simple(matrix=[]):
    square_matrix = [list(map(lambda i: i * i, row)) for row in matrix]
    return square_matrix