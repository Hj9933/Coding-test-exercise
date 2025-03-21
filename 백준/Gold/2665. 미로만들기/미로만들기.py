# 미로만들기
import sys
input = sys.stdin.readline
n = int(input())
graph = list(list(input()) for _ in range(n))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
import heapq
def dikjstra(x, y):
    q = []
    heapq.heappush(q,(0,(x, y)))
    distance[x][y] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                a = int(graph[nx][ny])
                if a == 0:
                    cost = 1 + dist
                else:
                    cost = dist
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))
INF = int(1e9)
distance = list([INF]*n for _ in range(n))
dikjstra(0,0)
print(distance[n-1][n-1])