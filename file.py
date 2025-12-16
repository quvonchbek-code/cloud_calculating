import numpy as np

matrix = np.random.randint(1, 101, size=(9, 9))
print(matrix)

def chetki_yigindi(matrix: np.ndarray) -> int:
    n, m = matrix.shape
    
    yigindi = matrix[0, :].sum() + matrix[n-1, :].sum()
    
    yigindi += matrix[1:n-1, 0].sum()
    yigindi += matrix[1:n-1, m-1].sum()
    
    return yigindi

def ikkala_diagonal_yigindi(matrix: np.ndarray) -> tuple[int, int]:
    
    asosiy = np.trace(matrix)
    qarama_qarshi = np.trace(np.fliplr(matrix))
    return asosiy + qarama_qarshi - matrix[4][4]
def aniq_romb_yigindi(matrix):
    n = matrix.shape[0]
    mid = n // 2
    yigindi = 0

    for i in range(n):
        for j in range(n):
            if abs(i - mid) + abs(j - mid) <= mid:
                yigindi += matrix[i][j]

    return yigindi
def ikkita_uchburchak_yigindi(matrix):
    n = matrix.shape[0]
    mid = n // 2
    yigindi = 0

    for i in range(n):
        if i <= mid:
            start = i
            end = n - i
        else:
            start = n - i - 1
            end = i + 1

        for j in range(start, end):
            yigindi += matrix[i][j]

    return yigindi
    
print("Eng chetki hadlarining yig`indisi : ",chetki_yigindi(matrix))
print("Diagonallarda joylashgan elementlar yig`indis : ",ikkala_diagonal_yigindi(matrix))
print("Uchinchi yuza yig`indisi : ",ikkita_uchburchak_yigindi(matrix))
print("To'rtinchi yuza yig`indisi : ", aniq_romb_yigindi(matrix))
