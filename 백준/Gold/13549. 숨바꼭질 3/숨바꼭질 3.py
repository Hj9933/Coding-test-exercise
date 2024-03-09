import sys
input = sys.stdin.readline

# 갈 수 있는 방법은 총 3가지 (x-1, 1), (x+1, 1), (2*x, 0)
# 모든 점에 대해 갈 수 있는 경로로 그래프를 만든 다음, 다익스트라 알고리즘을 통해 풀 수 있음
import heapq

n, k = map(int, input().split())
# 가능한 점이 100000개 이므로 이 점들에 대한 그래프 생성
graph = [[] for _ in range(100001)]
graph[0].append((1,1))
graph[1].append((0,1))
graph[1].append((2,0)) # +1을 하는 경우와 *2를 하는 경우가 같아져서 비용이 더 작은 쪽으로 

for i in range(2, 100001):
    graph[i].extend([(i-1, 1), (i+1, 1), (2*i, 0)])

INF = int(1e9)
distance = [INF]*(100001)
# 다익스트라 알고리즘 구현
def dikjstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 간적이 있다면 무시
            continue
        for i in graph[now]: # 갈 수 있는 노드들에 대한 코스트 계산해서 코스트가 원래보다 더 작으면 대체하고 큐에 넣기
            cost = dist + i[1]
            if 0 <= i[0] <= 100000 and cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dikjstra(n)
print(distance[k])