import sys
input = sys.stdin.readline

# 1261. 알고스팟
from collections import deque
import heapq

m, n = map(int, input().split())
graph = [list(input()) for _ in range(n)]
INF = int(10**9)
distance = [[INF]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dikjstra(x, y):
    q = []
    heapq.heappush(q, (0,x,y))

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                cost = dist + int(graph[nx][ny])
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

dikjstra(0,0)
if distance[n-1][m-1] == INF:
    print(0)
else:
    print(distance[n-1][m-1])