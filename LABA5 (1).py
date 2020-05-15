import numpy as np

def count_average(matrix1, matrix2):
    rez = 0.0
    rez += matrix1[1]/matrix2[1] + matrix1[0]/matrix2[0] + matrix1[2]/matrix2[2]
    return rez/3.0


def normalize(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
       return vector
    return vector / norm


def LABA5(matrix):
    epsilon = 0.001
    A = np.array(matrix)
    y = np.array([[1.0], [1.0], [1.0]])
    tmp = []
    tmp.append(A.dot(y))
    tmp.append(A.dot(tmp[-1]))
    tmp.append(A.dot(tmp[-1]))
    i = 3
    while 1 < i:
        tmp.append(A.dot(tmp[-1]))
        first = tmp[-1]
        second = tmp[-2]
        third = tmp[-3]

        avg1 = count_average(first, second)
        avg2 = count_average(second, third)

        if (abs(avg1 - avg2) < epsilon):
            #normedvec = normalize(first)
            #print(normedvec)
            break

        i+=1

    return [avg1, i];


print(LABA5([[4.0, 1.0, 0.0], [1.0, 2.0, 1.0], [0.0, 1.0, 1.0]]))
print(LABA5([[2.0, 1.0, -4.0], [-3.0, 4.0, 0.0], [-3.0, -1.0, 8.0]]))
print(LABA5([[1.0, -3.0, -2.0],[-1.0,4.0,4.0],[-2.0,3.0,6.0]]))
print(LABA5([[-1.0,7.0,2.0], [9.0,8.0,1.0], [5.0,2.0,7.0]]))
print(LABA5([[-10.0,1.0, -1.0],[-4.0, -8.0, -1.0], [-2.0, -5.0, -9.0]]))