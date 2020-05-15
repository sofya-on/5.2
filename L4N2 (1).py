import numpy as np
import sys 

def Swap_Rows(matrix: np.array) -> bool:
    for i in range(len(matrix)):
        if matrix[i, 0] != 0:
            matrix[0, :], matrix[i, :] = matrix[i, :], matrix[0, :].copy()
            return True
    return False


def Swap_Cols(matrix: np.array) -> bool:
    for i in range(len(matrix)):
        if matrix[0, i] != 0:
            matrix[:, 0], matrix[:, i] = matrix[:, i], matrix[:, 0].copy()
            return True
    return False


def Block_Split(matrix: list, slice_x: int, slice_y: int) -> tuple:
    matrix = np.asfarray(matrix)
    return matrix[0:slice_x, 0:slice_y],  \
           matrix[0:slice_x, slice_y:],   \
           matrix[slice_x:, 0:slice_y],   \
           matrix[slice_x:, slice_y:]


def Inv_Matrix(matrix: list) -> list:
    slice_index = 1
    matrix = np.asfarray(matrix.copy())
    arr = Block_Split(matrix, slice_index, slice_index)
    return Inv_Matrix_Recursive(matrix, list(arr[0]), slice_index)


def Inv_Matrix_Recursive(matrix: list, s, slice_index) -> list:
    if slice_index > len(matrix):
        return s
    if Det(s) == 0:
        swapped = Swap_Rows(matrix)
        if not swapped:
            return list()
    arr = Block_Split(matrix, slice_index, slice_index)
    if slice_index == 1:
        return Inv_Matrix_Recursive(matrix,
                                        list(1.0 / arr[0]),
                                        slice_index + 1)
    ind = len(arr[0]) - 1
    a_11, a_12, a_21, a_22 = Block_Split(arr[0], ind, ind)
    a_inv = s
    x = np.array(a_inv @ a_12)
    y = np.array(a_21 @ a_inv)
    if ((a_22 - y @ a_12) != 0):
        teta_inv = np.array(1 / (a_22 - y @ a_12))
    else:
        return print("failed to get reverse theta =>")
    s = np.bmat([[a_inv + x @ teta_inv @ y, -x @ teta_inv],
                 [-teta_inv @ y, teta_inv]])
    return Inv_Matrix_Recursive(matrix, s, slice_index + 1)


def Det(matrix: list) -> float:
    matrix = np.asfarray(matrix.copy())
    first = matrix[0, 0]
    if len(matrix) == 1:
        return first
    if first == 0:
        swapped = Swap_Cols(matrix)
        first = -matrix[0, 0]
        if not swapped:
            return 0
    matrix[:, 0] /= first
    for i in range(1, len(matrix)):
        i_first = matrix[0, i]
        matrix[:, i] -= matrix[:, 0] * i_first
    return first * Det(matrix[1:, 1:])


print(Inv_Matrix(np.array([[1, -2,], [3, -2]])))
print(Inv_Matrix(np.array([[1, 4, 1, 3], [0, -1, 3, -1], [3, 1, 0, 2], [1, -2, 5, 1]])))
print(Inv_Matrix(np.array([\
    [-2.0, -1.0, -2.0, -2.0, -3.0],\
    [4.0,  2.0,  4.0,  5.0,  -4.0],\
    [1.0,  -1.0, 0.0,  3.0,  -3.0],\
    [2.0,  2.0,  2.0,  -4.0, -3.0],\
    [0.0,  -1.0, 2.0,  1.0,  4.0]])))
