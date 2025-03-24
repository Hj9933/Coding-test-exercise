# 파이프 옮기기1
import sys
input = sys.stdin.readline
n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

def dfs(s1, e1, s2, e2):
    global cnt
    visited[s2][e2] = True
    if s2 == n-1 and e2 == n-1:
        cnt += 1
        return
    if s1 == s2: # 가로
        nx, ny = s2, e2+1
        if ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(s2, e2, nx, ny)
            visited[nx][ny] = False
        nx, ny = s2+1, e2+1
        if nx < n and ny < n and not visited[nx][ny] and graph[nx][ny] == 0 and graph[nx-1][ny] == 0 and graph[nx][ny-1] == 0:
            dfs(s2, e2, nx, ny)
            visited[nx][ny] = False
    elif e1 == e2: # 세로
        nx, ny = s2+1, e2
        if nx < n and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(s2, e2, nx, ny) 
            visited[nx][ny] = False       
        nx, ny = s2+1, e2+1
        if nx < n and ny < n and not visited[nx][ny] and graph[nx][ny] == 0 and graph[nx-1][ny] == 0 and graph[nx][ny-1] == 0:
            dfs(s2, e2, nx, ny)
            visited[nx][ny] = False
    else: # 대각선
        nx, ny = s2, e2+1
        if ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(s2, e2, nx, ny)
            visited[nx][ny] = False
        nx, ny = s2+1, e2+1
        if nx < n and ny < n and not visited[nx][ny] and graph[nx][ny] == 0 and graph[nx-1][ny] == 0 and graph[nx][ny-1] == 0:
            dfs(s2, e2, nx, ny)
            visited[nx][ny] = False
        nx, ny = s2+1, e2
        if nx < n and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(s2, e2, nx, ny)   
            visited[nx][ny] = False
visited = list([False]*n for _ in range(n))
cnt = 0
visited[0][0] = True
dfs(0,0,0,1)
print(cnt)