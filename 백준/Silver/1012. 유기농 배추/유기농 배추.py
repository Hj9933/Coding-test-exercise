import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(x,y):
    if x >= m or x <= -1 or y >= n or y <= -1:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0 # 방문처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                result += 1
    print(result)
