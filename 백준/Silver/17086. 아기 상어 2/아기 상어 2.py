# 17086. 아기상어2
n, m = map(int, input().split())

maps = list(list(map(int, input().split())) for _ in range(n))

from collections import deque

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,-1,-1,1]
def bfs(x,y):
    q = deque([])
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m and visited[nx][ny] == -1:
                if maps[nx][ny] == 1:
                    return visited[x][y] + 1
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return False
ans = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            visited = list([-1]*m for _ in range(n))
            ans = max(ans, bfs(i,j))
print(ans)