import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 10026. 적록색약
n = int(input())
graph = [list(input()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,visited, c, rgb=True):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == c:
                dfs(nx,ny,visited,c)
    return True

visited = [[False]*n for _ in range(n)]
cnt_RGB = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if dfs(i, j, visited, graph[i][j]):
                cnt_RGB += 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False]*n for _ in range(n)]
cnt_noRGB = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if dfs(i, j, visited, graph[i][j], rgb=False):
                cnt_noRGB += 1
print(cnt_RGB, cnt_noRGB)