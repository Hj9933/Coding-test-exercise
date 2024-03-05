# 개선된 다익스트라 알고르즘으로 풀기
import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start =int(input())
INF = int(1e9) # 무한을 10억으로 설정
distance = [INF]*(v+1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split()) # a에서 b로 가는 가중치 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작지점은 최단경로를 0으로 설정하여 힙에 집어넣기
    distance[start] = 0
    while q: # q가 비어있지 않으면
        dist, now = heapq.heappop(q) # 가장 우선순위의(가장 거리가 짧은) 요소를 꺼내옴
        if distance[now] < dist: # 이미 처리된 적이 있다면 무시
            continue
        for i in graph[now]: # 인접한 노드들의 비용 계산
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 거리가 더 짧으면 힙에 넣기

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

