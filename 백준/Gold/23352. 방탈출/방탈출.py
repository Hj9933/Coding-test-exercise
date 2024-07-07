import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
from collections import deque
def bfs(x,y):
    q = deque([])
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0: # 들어갈 수 없는 방이면 pass
                continue
            elif visited[nx][ny] != 0: # 이미 방문한 방이면 pass
                continue
            else:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return x, y

secret = 0
dist = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            visited = [[0]*m for _ in range(n)]
            x_f, y_f  = bfs(i, j)
            if visited[x_f][y_f] > dist:
                dist = visited[x_f][y_f]
                secret = graph[i][j] + graph[x_f][y_f]
            elif visited[x_f][y_f] == dist:
                secret = max(secret, graph[i][j] + graph[x_f][y_f])

print(secret)