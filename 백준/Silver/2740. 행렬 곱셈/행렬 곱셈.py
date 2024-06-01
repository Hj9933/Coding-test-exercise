import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
m, k = map(int, input().split())
B = list(list(map(int, input().split())) for _ in range(m))

c = list([0]*k for _ in range(n))
for i in range(n):
    for l in range(k):
        temp = 0
        for j in range(m):
            temp += A[i][j]*B[j][l]
        c[i][l] = temp
for i in range(n):
    for j in range(k):
        print(c[i][j], end = ' ')
    print()
        
