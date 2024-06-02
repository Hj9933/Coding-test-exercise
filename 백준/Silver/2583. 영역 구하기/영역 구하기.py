import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
lst = list(list(map(int, input().split())) for _ in range(k))
for i in range(m):
    for j in range(n):
        for l in range(k):
            if i >= m - lst[l][3] and i < m - lst[l][1] and j >= lst[l][0] and j < lst[l][2]:
                graph[i][j] = 1

def dfs(x,y, visited):
    global temp
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 0 and visited[x][y] == 0:
        visited[x][y] = 1
        temp += 1
        dfs(x-1, y, visited)
        dfs(x+1, y, visited)
        dfs(x, y-1, visited)
        dfs(x, y+1, visited)
        return True
    return False

visited = [[0]*n for _ in range(m)]
cnt = 0
result = []
for i in range(m):
    for j in range(n):
        temp = 0
        if dfs(i,j,visited) == True:
            cnt += 1
            result.append(temp)
print(cnt)
for p in sorted(result):
    print(p, end=' ')
                