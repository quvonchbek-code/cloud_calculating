N = 9

def calculate_sum_b(A: list[list[int]], N: int) -> int:
    s = 0
    
    for i in range(N):
        for j in range(N):
            if i  == j or i + j == N - 1:
                s += A[i][j]
                
    return s

def calculate_sum_e(A: list[list[int]], N: int) -> int:
    center = N // 2       
    radius = N // 2       
    
    s = 0
    
    for i in range(N):
        for j in range(N):
            if abs(i - center) + abs(j - center) <= radius:
                s += A[i][j]
    
    return s



A = [[1 for j in range(N)] for i in range(N)]

s_b = calculate_sum_b(A, N)
print(f"b shakl yuzasi: {s_b}")

s_e = calculate_sum_e(A, N)
print(f"e shaklyuzasi: {s_e}")

