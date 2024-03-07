import sys
input = sys.stdin.readline


from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 목표지점인 2에서부터 시작해야하므로 2의 위치 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x = i
            y = j
            break

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 너비 우선 탐색 알고리즘
def bfs(queue):
    global one
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0: # 갈 수 없는 땅이면 무시
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                if graph[nx][ny] == 1:
                    one.append((nx, ny))
                queue.append((nx, ny))
    return one
queue = deque()
queue.append((x, y))
graph[x][y] = 0 # 초기 지점 0으로 초기화

one = []
one = bfs(queue)
for i in range(len(one)):
    x_one, y_one = one[i]
    graph[x_one][y_one] = 1

# 갈 수 있는 땅이지만 도달할 수 없는 위치는 -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and ((i, j) not in one):
            graph[i][j] = -1

# 그래프 출력
for row in graph:
    print(*row)