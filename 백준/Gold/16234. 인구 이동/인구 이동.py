import sys
input = sys.stdin.readline

from collections import deque

# BFS 함수 정의
def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    temp = [(x, y)]
    visited[x][y] = True
    total_population = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    temp.append((nx, ny))
                    total_population += graph[nx][ny]
                    count += 1

    # 연합 인구수 업데이트
    new_population = total_population // count
    for x, y in temp:
        graph[x][y] = new_population

    return count > 1

# 입력
n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

while True:
    visited = [[False] * n for _ in range(n)]
    is_moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    is_moved = True

    if not is_moved:
        break

    result += 1

print(result)
