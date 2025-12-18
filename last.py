import numpy as np

matrix = np.random.randint(1, 101, size=(9, 9))
print(matrix)


def aniq_romb_yigindi(matrix):
    n = matrix.shape[0]
    mid = n // 2
    yigindi = 0

    for i in range(n):
        for j in range(n):
            if abs(i - mid) + abs(j - mid) <= mid:
                yigindi += matrix[i][j]

    return yigindi

def ikkala_diagonal_yigindi(matrix: np.ndarray) -> tuple[int, int]:
    
    asosiy = np.trace(matrix)
    qarama_qarshi = np.trace(np.fliplr(matrix))
    return asosiy + qarama_qarshi - matrix[4][4]

    

print("Diagonallarda joylashgan elementlar yig`indis : ",ikkala_diagonal_yigindi(matrix))
print("To'rtinchi yuza yig`indisi : ", aniq_romb_yigindi(matrix))
