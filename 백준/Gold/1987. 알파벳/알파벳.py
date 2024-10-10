import sys
input = sys.stdin.readline
# 1987. 알파벳
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    q = set([(x,y, graph[x][y])])
    answer = 0
    while q:
        x, y, alphabet = q.pop()
        answer = max(answer, len(alphabet))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not graph[nx][ny] in alphabet:
                    q.add((nx, ny, alphabet+graph[nx][ny]))
                    
    return answer

answer = bfs(0,0)
print(answer)