import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = list([] for _ in range(n+1))
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
A, B = map(int, input().split())

def dikjstra(start, distance):
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

INF = int(1e9)
distance = [INF]*(n+1)
dikjstra(A, distance)
print(distance[B])