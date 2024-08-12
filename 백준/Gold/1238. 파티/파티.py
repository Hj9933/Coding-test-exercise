import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

import heapq
INF = int(1e9)
distance = [INF]*(n+1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
result = [0]*(n+1)
for i in range(1,n+1):
    distance = [INF]*(n+1)
    dijkstra(i) # 집 -> x
    result[i] += distance[x]
    distance = [INF]*(n+1)
    dijkstra(x) # x -> 집
    result[i] += distance[i]
print(max(result[1:]))