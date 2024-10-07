# 2589 보물섬
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y, visited):
    q = deque([])
    q.append((x, y))
    visited[x][y] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and graph[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx, ny))
    return cnt
cnt = 0
for k in range(n):
    for l in range(m):
        if graph[k][l] == 'L':
            visited = [[-1]*m for _ in range(n)]
            cnt = max(cnt, bfs(k,l, visited))

print(cnt)