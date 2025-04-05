import sys
input = sys.stdin.readline
import heapq
n, m = map(int, input().split())
graph = list([(i+1,1),(i+2,1),(i+3,1),(i+4,1),(i+5,1),(i+6,1)] for i in range(95))
graph.append([(96,1),(97,1),(98,1),(99,1),(100,1)])
graph.append([(97,1),(98,1),(99,1),(100,1)])
graph.append([(98,1),(99,1),(100,1)])
graph.append([(99,1),(100,1)])
graph.append([(100,1)])
graph.append([])

for _ in range(n+m):
    a, b = map(int, input().split())
    graph[a] = [(b,0)]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

INF = int(1e9)
distance = [INF]*101
dijkstra(1)
print(distance[100])