import sys
# input = sys.stdin.readline()
n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
def bfs_air(x,y):
    q = deque([(x,y)])
    visited_air[x][y] = True
    tmp_graph_air[x][y] = -1
    while q:
        now = q.popleft()
        x, y = now[0], now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited_air[nx][ny]:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited_air[nx][ny] = True
                    tmp_graph_air[nx][ny] = -1
def melt(x,y):
    melt_y = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tmp_graph_air[nx][ny] == -1:
            melt_y = True
            break
    if melt_y:
        tmp_graph[x][y] = 1


def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        now = q.popleft()
        x, y = now[0], now[1]
        melt(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] += visited[x][y]
                    cnt += 1
    return cnt

time = 0
result = []
while True:
    time += 1
    visited_air = list([False]*m for _ in range(n))
    tmp_graph_air = list([0]*m for _ in range(n))
    bfs_air(0,0)
    visited = list([False]*m for _ in range(n))
    cnt = 0
    for i in range(n):
        for j in range(m):
            tmp_graph = list([0]*m for _ in range(n))
            if graph[i][j] == 1 and not visited[i][j]:
                tmp = bfs(i,j)
                cnt += tmp
                for k in range(n):
                    for l in range(m):
                        graph[k][l] -= tmp_graph[k][l]
    result.append(cnt)
    total = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                total += 1
    if total == n*m:
        break
 
    
            
print(time)
print(result[-1])          