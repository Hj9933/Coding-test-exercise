# 1303. 전쟁-전투
import sys
input = sys.stdin.readline
# 1303. 전쟁-전투
n, m = map(int, input().split())
graph = list(list(input()) for _ in range(m))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x, y, team):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == team:
                dfs(nx, ny, team)

cnt_W = 0
visited = list([False]*n for _  in range(m))
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            cnt = 0
            dfs(i,j,team = 'W')
            cnt_W += cnt**2
cnt_B = 0
visited = list([False]*n for _  in range(m))
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'B' and not visited[i][j]:
            cnt = 0
            dfs(i,j,team = 'B')
            cnt_B += cnt**2

print(cnt_W, cnt_B, end=' ')