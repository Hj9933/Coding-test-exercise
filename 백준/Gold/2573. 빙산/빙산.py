import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
# 2573 빙산
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and graph[nx][ny] != 0:
                dfs(nx, ny, visited)
    return True
def iceberg(x,y):
    tmp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                tmp += 1
    tmp_graph[x][y] = tmp


cnt = 0
result = 0
while cnt < 2:
    tmp_graph = [[0]*m for _ in range(n)]
    for k in range(n):
        for l in range(m):
            if graph[k][l] != 0:
                iceberg(k, l)
    for k in range(n):
        for l in range(m):
            if graph[k][l] - tmp_graph[k][l] >= 0:
                graph[k][l] -= tmp_graph[k][l]
            else:
                graph[k][l] = 0
    result += 1
    visited = [[False]*m for _ in range(n)]
    zero_cnt = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                zero_cnt += 1
            else:
                if not visited[i][j]:
                    if dfs(i,j,visited):
                        cnt += 1
    if zero_cnt == n*m:
        break

if zero_cnt == n*m:
    print(0)
else:
    print(result)