import sys
input = sys.stdin.readline
n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,k):
    q = deque([])
    q.append((x,y))
    graph1[x][y] = k
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not graph1[nx][ny]:
                graph1[nx][ny] = k
                q.append((nx,ny))

graph1 = list([False]*n for _ in range(n))
k = 1
for i in range(n):
    for j in range(n):
        if not graph1[i][j] and graph[i][j] == 1:
            bfs(i,j, k)
            k += 1
def bfs2(island):
    q = deque([])
    dist = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph1[i][j] == island:
                q.append((i,j))
                dist[i][j] = 0
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph1[nx][ny] != island and graph1[nx][ny] != False: # 다른 섬과 만났을 때
                    return dist[x][y]
                if graph1[nx][ny] == False and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return False
result = int(1e9)
for island in range(1, k+1):
    tmp = bfs2(island)
    if tmp:
        result = min(result, bfs2(island))

print(result)
