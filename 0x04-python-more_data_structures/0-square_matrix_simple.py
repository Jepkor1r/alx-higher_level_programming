#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[element * element for element in row] for row in matrix]

matrix = []
squaredMatrix = map(square_matrix_simple, matrix)
print(squaredMatrix)
