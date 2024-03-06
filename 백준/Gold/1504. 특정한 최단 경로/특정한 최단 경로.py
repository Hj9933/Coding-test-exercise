import sys
input = sys.stdin.readline

# 다익스트라 알고리즘 시도
# min(1-v1 + v1-v2 + v2-N, 1-v2 + v2-v1 + v1-N)
import heapq
n, e = map(int, input().split())
# 무한으로 초기화된 리스트
INF = int(1e9)
distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 지나야되는 정점
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
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

# start = [1, v1, v2] 총 3번의 알고리즘 수행해야함
distance = [INF] * (n+1)
dijkstra(1)
dist_1_v1 = distance[v1]
dist_1_v2 = distance[v2]

distance = [INF] * (n+1)
dijkstra(v1)
dist_v1_v2 = distance[v2]
dist_v1_N = distance[n]

distance = [INF] * (n+1)
dijkstra(v2)
dist_v2_v1 = distance[v1]
dist_v2_N = distance[n]

dist = min(dist_1_v1+dist_v1_v2+dist_v2_N, dist_1_v2+dist_v2_v1+dist_v1_N)
if dist >= INF:
    print(-1)
else:
    print(dist)