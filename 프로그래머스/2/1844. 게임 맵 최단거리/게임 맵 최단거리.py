from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if maps[nx][ny] != 1:
                    continue
                else:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1 # 방문처리        
    bfs(0,0)
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
    return answer