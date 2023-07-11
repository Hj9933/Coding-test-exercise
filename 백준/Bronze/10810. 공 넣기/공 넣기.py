n, m = map(int, input().split())
ijk = [list(map(int, input().split())) for _ in range(m)]

A = [0] * n
for i in range(m):
    for j in range(ijk[i][0]-1, ijk[i][1]):
        A[j] = ijk[i][2]
        
for i in range(n):
    print(A[i], end = " ")