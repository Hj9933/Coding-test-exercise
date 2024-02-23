import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            x = i
            y = j
            break


dx = [-1,1,0,0] 
dy = [0,0,-1,1]
cnt = 0
def dfs(x,y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >=m:
        return cnt
    if graph[x][y] == 'O' or graph[x][y] == 'I':
        graph[x][y] = 'X' # 방문처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return cnt
    elif graph[x][y] == 'P' or graph[x][y] == 'I':
        graph[x][y] = 'X' # 방문처리
        cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return cnt
    return cnt

cnt = dfs(x,y)

if cnt == 0:
    print('TT')
else:
    print(cnt)