import sys
input = sys.stdin.readline

import heapq
n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
INF = int(1e9)
distance = [INF]*(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist: # 현재 노드의 distance가 INF가 아니라면 이미 처리된 적이 있는 것 -- 맞나..? 질문!
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(s)
result = distance[e]
if result == INF:
    print(-1)
else:
    print(result)