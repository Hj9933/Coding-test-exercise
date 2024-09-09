import sys
input = sys.stdin.readline
# 로봇청소시
n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 0:북, 1:동, 2:남, 3:서
graph = list(list(map(int, input().split())) for _ in range(n))

cnt = 0
dx = [-1,0,1,0] # 북, 동, 남, 서 순으로
dy = [0,1,0,-1]
while True:
    if graph[r][c] == 0: # 현재 청소되지 않은 빈칸이면 청소(2)
        graph[r][c] = 2
        cnt += 1
    temp = 0
    for i in range(4): # 현재 칸 주변 4칸 중 청소되지 않은 벽이 있는지 검사
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if graph[nx][ny] == 0:
                temp += 1
    if temp == 0: # 주변 4칸 중 청소되지 않은 벽이 없다면 후진
        r = r - dx[d]
        c = c - dy[d]
        if r < 0 or r >= n or c < 0 or c >= m:
            break
        if graph[r][c] == 1: # 뒤쪽칸이 벽이면 작동 멈춤
            break
    else: # 청소되지 않은 벽이 있다면 반시계방향으로 회전
        d -= 1
        if d < 0:
            d = 3
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if graph[nx][ny] == 0:
                r = nx
                c = ny
print(cnt)