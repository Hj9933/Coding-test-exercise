# 서강 그라운드
import sys
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = list([] for _ in range(n+1))
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
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
ans = 0
for i in range(1,n+1):
    distance = [INF]*(n+1)
    dijkstra(i)
    tmp = 0
    for i in range(1,n+1):
        if distance[i] <= m:
            tmp += items[i-1]
    ans = max(tmp, ans)
print(ans)