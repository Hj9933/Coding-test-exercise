# 1520. 내리막길
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

dx = [1,0,-1,0]
dy = [0,1, 0, -1]
dp = [[-1]*m for _ in range(n)]
def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    ans = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < graph[x][y]:
            ans += dfs(nx,ny)
    dp[x][y] = ans
    return ans
print(dfs(0,0))
