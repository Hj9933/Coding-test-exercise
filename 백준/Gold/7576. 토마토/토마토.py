from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == -1: # 토마토가 들어가있지 않으면 무시
                continue
            elif graph[nx][ny] == 0: # 익지 않은 토마토가 들어있다면 익히기
                graph[nx][ny] = graph[x][y] + 1
                result  = graph[nx][ny]
                queue.append((nx, ny))
    return graph

cnt = 0
cnt_1 = 0 # 익지 않은 토마토 개수
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            queue.append((i, j))
        elif graph[i][j] == -1:
            cnt_1 += 1

graph_after = bfs(queue)
res = 0
flag = False # 익지 않은 토마토 여부

for i in graph_after:
    for j in i:
        # 익지 않은 토마토가 있다면
        if j == 0:
            flag = True
    res = max(res, max(i))

if cnt == n*m - cnt_1: # 처음부터 모든 토마토가 익어있는 상태
    print(0)
elif  flag == True: # 익지 않은 토마토가 있다면
    print(-1)
else:
    print(res-1)