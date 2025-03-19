# 숫자 정사각형
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rectan = list(list(input()) for _ in range(n))
ans = 1
for i in range(n):
    for j in range(m):
        for k in range(1,m):
            if i+k < n and j+k < m:
                a = rectan[i][j]
                if rectan[i][j+k] == a and rectan[i+k][j] == a and rectan[i+k][j+k] == a:
                    ans = max(ans, (k+1)*(k+1))
print(ans)