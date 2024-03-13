import sys
input = sys.stdin.readline

t = int(input())
lst = [[] for _ in range(t)]
for i in range(t):
    for _ in range(2):
        lst[i].append(int(input()))
# 각 케이스별로 (k, n+1)의 d 생성; k층 n호; 호는 0호가 없으므로 n+1개 생성
for k, n in lst:
    d = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1,n+1): # 0층은 i호에 i명 살고있음
        d[0][i] = i 
    for j in range(1, k+1):
        for a in range(1, n+1):
            d[j][a] = sum(d[j-1][:a+1])
    print(d[k][n])