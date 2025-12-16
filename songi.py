import numpy as np

matrix = np.random.randint(1, 101, size=(9, 9))
print(matrix)

def chetki_yigindi(matrix: np.ndarray) -> int:
    n, m = matrix.shape
    
    yigindi = matrix[0, :].sum() + matrix[n-1, :].sum()
    
    yigindi += matrix[1:n-1, 0].sum()
    yigindi += matrix[1:n-1, m-1].sum()
    
    return yigindi

def aniq_romb_yigindi(matrix):
    n = matrix.shape[0]
    mid = n // 2
    yigindi = 0

    for i in range(n):
        for j in range(n):
            if abs(i - mid) + abs(j - mid) <= mid:
                yigindi += matrix[i][j]

    return yigindi