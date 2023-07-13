def square_matrix_simple(matrix=[]):
    square_matrix = []
    for fila in matrix:
        nueva_fila = []
        for i in fila: 
            nueva_fila.append(i ** 2)
        square_matrix.append(nueva_fila)
    return square_matrix