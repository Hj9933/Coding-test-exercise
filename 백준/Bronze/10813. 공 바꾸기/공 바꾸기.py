N, M = map(int, input().split())
ex = [list(map(int, input().split())) for _ in range(M)]
a = list(i for i in range(1,N+1))

for i in range(M):
    b = a[ex[i][0] - 1]
    c = a[ex[i][1] - 1]
    a[ex[i][0] - 1] = c
    a[ex[i][1] - 1] = b

for i in range(N):
    print(a[i], end = " ")
    