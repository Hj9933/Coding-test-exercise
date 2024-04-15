import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(1, v+1):
    tmp = list(map(int, input().split()))
    i = tmp[0]
    for j in range(1, len(tmp)-1, 2):
        graph[i].append((tmp[j], tmp[j+1]))

import heapq
# 최장거리를 구해야하므로 최대 힙 이용한 다익스트라 알고리즘 사용
def dikjstra(start, visited):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    visited[start] = True
    while q:
        dist, now = heapq.heappop(q)
        visited[now] = True
        if distance[now] > -dist:
            continue
        for i in graph[now]:
            cost = -dist + i[1]
            if visited[i[0]] == False and cost > distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (-cost, i[0]))


# 리프 노드를 구할 필요 없음. 먼저 1번 노드에 대해서 함수 실행 후 가장 먼 노드를 찾고 그 노드에서 다시 함수 실행
visited = [False]*(v+1)
distance = [-1]*(v+1)
dikjstra(1, visited)
start = distance.index(max(distance))
visited = [False]*(v+1)
distance = [-1]*(v+1)
dikjstra(start, visited)
print(max(distance))
