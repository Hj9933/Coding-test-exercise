import sys
input = sys.stdin.readline
# 여행가자
n = int(input())
m = int(input())

## 플루이드 워셜
graph = [[0]*(n+1)]
for i in range(n):
    graph.append([0]+list(map(int,input().split())))
destination = list(map(int, input().split()))

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
for i in range(1,n+1):
    graph[i][i] = 1

start = destination[0]
flag = True
for i in range(1, len(destination)):
    x = destination[i]
    if graph[start][x] == 0:
        flag = False
        break
    start = destination[i]
if flag:
    print("YES")
else:
    print("NO")
