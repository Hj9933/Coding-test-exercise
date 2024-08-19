import sys
input = sys.stdin.readline

# 연구소- bfs+조합
n, m = map(int, input().split())
map = list(list(map(int, input().split())) for _ in range(n))


# 0과 2의 위치 저장 / 1 개수 세기
zero = []
two = []
one = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            zero.append((i,j))
        elif map[i][j] == 2:
            two.append((i,j))
        elif map[i][j] == 1:
            one += 1

# BFS
from collections import deque
import copy
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    global safe
    safe -= 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                safe -= 1
                q.append((nx,ny))
    return safe

from itertools import combinations
result = 0
for comb in combinations(zero, 3):
    temp = copy.deepcopy(map)
    for i in range(3):
        temp[comb[i][0]][comb[i][1]] = 1
    safe = n*m
    for t in two:
        safe = bfs(t[0],t[1])
    result = max(result, safe)
        
print(result - one - 3)