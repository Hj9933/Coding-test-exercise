import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 그림
n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    global cnt
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                cnt += 1
                # print(nx,ny)
                dfs(nx, ny)

visited = list([False]*m for _ in range(n))
max_cnt = 0
result = 0
for j in range(n):
    for k in range(m):
        if graph[j][k] == 1 and visited[j][k] == False:
            cnt = 1
        
            dfs(j,k)
            max_cnt = max(max_cnt, cnt)
            if cnt > 0:
                result += 1

print(result)
print(max_cnt)