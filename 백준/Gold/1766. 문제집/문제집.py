import sys
input = sys.stdin.readline

# 위상정렬
# 조건을 만족시키면서 작은 수를 우선적으로 풀어야하므로 우선순위 큐를 사용해야 할 듯
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = []
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0: # 진입차수가 0인 노드들 힙큐에 넣기
            heapq.heappush(q, i)
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)
    print(*result)
topology_sort()