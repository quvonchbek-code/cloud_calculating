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
    """
    Asosiy va qarama-qarshi diagonal yig'indilarini qaytaradi.
    """
    asosiy = np.trace(matrix)
    qarama_qarshi = np.trace(np.fliplr(matrix))
    return asosiy + qarama_qarshi - matrix[4][4]

print("Eng chetki hadlarining yig`indisi : ",chetki_yigindi(matrix))
print("Diagonallarda joylashgan elementlar yig`indis : ",ikkala_diagonal_yigindi(matrix))