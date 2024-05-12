import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1: # 섬이면 방문
        graph[x][y] = 0 # 방문 표시
        # 대각선도 가능하므로 총 8가지
        dfs(x-1, y)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

while True:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)
