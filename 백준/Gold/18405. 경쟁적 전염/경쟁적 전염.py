import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
s, x, y = map(int, input().split())
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))
virus.sort()
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(s, x, y):
    q = deque(virus)
    t = 0
    while q:
        if t == s:
            break
        for _ in range(len(q)):
            now, X, Y = q.popleft()
            for i in range(4):
                nx = X + dx[i]
                ny = Y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[X][Y]
                        q.append((graph[nx][ny], nx,ny))
        t += 1
    return graph[x-1][y-1]

print(bfs(s, x, y))