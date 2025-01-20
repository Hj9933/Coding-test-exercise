n, k = map(int, input().split())

import heapq
from collections import deque

d = ['-','+','*']
def bfs(x, cnt):
    min_time = 0
    num = 0
    q = deque()
    q.append((x, cnt))
    visited[x] = 1

    while q:
        x, cnt = q.popleft()
        visited[x] = 1

        if x == k:
            if min_time == 0:
                min_time = cnt
                num += 1
            elif min_time == cnt:
                num += 1
            else:
                break
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx <= 100000:
                if visited[nx] == 0:
                    q.append((nx, cnt+1))
    return min_time, num

visited = [0]*100001
for i in bfs(n,0):
    print(i)