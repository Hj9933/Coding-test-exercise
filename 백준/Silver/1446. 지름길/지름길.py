# 1446. 지름길
import sys
input = sys.stdin.readline
n, d = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
graph = list([(i+1,1)] for i in range(10001))
for i in range(n):
    graph[lst[i][0]].append((lst[i][1],lst[i][2]))
INF = int(1e9)
distance = [INF]*10001

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if i[0] > d:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(0)
print(distance[d])
