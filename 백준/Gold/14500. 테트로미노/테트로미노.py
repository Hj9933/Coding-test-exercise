import sys
input = sys.stdin.readline

# 현재 블록의 위치에서 모든 위치를 탐방하면서 4개가 되면 그때의 점수 확인 -> dfs
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n, m = map(int,input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
maxx = 0
# ㅗ 모양 제외하고 탐방
def dfs(x, y, level, visited, cnt):
    global maxx
    if level == 4:
        if cnt > maxx:
            maxx = cnt
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <=ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, level+1, visited, cnt+graph[nx][ny])
            visited[nx][ny] = False
# ㅗ 모양
def exce(x, y):
    global maxx
    for i in range(4):
        tmp = graph[x][y]
        for j in range(3):
            t = (i+j)%4
            nx = x + dx[t]
            ny = y + dy[t]

            if not ( 0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += graph[nx][ny]
        maxx = max(maxx, tmp)
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, visited, graph[i][j])
        visited[i][j] = False

        exce(i, j)

print(maxx)