import numpy as np

def counter(matrix1, matrix2):
    res = 0.0
    res += matrix1[1]/matrix2[1] + matrix1[0]/matrix2[0] + matrix1[2]/matrix2[2]
    return res/3.0

def MAXS(matrix):
    A = np.array(matrix)
    y = np.array([[1.0], [1.0], [1.0]])
    tmp = []
    e = 0.001
    tmp.append(A.dot(y))
    tmp.append(A.dot(tmp[-1]))
    tmp.append(A.dot(tmp[-1]))
    i = 3
    while 1 < i:
        tmp.append(A.dot(tmp[-1]))
        a = tmp[-1]
        b = tmp[-2]
        c = tmp[-3]

        s1 = counter(a, b)
        s2 = counter(b, c)

        if (abs(s1 - s2) < e):
            break
            
        i+=1
        
    return [s1, i];

print(MAXS([[2.0, 1.0, -4.0], [-3.0, 4.0, 0.0], [-3.0, -1.0, 8.0]]))
print(MAXS([[1.0, -3.0, -2.0],[-1.0,4.0,4.0],[-2.0,3.0,6.0]]))
print(MAXS([[-1.0,7.0,2.0], [9.0,8.0,1.0], [5.0,2.0,7.0]]))
print(MAXS([[-10.0,1.0, -1.0],[-4.0, -8.0, -1.0], [-2.0, -5.0, -9.0]]))
