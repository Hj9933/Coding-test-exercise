N, M = map(int, input().split())

rev = [list(map(int, input().split())) for _ in range(M)]
A = list(i+1 for i in range(N))
for i in range(M):
    a = rev[i][0] - 1
    b = rev[i][1] 
    A[a:b] = list(reversed(A[a:b]))

for j in range(N):
    print(A[j], end = " ")
