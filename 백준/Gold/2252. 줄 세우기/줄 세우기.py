import sys
input = sys.stdin.readline

# 위상정렬
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, n+1): # 진입차수가 0인 노드 모두 큐에 넣기
        if indegree[i] == 0:
            q.append(i)
    while q: # 큐가 빌 때까지
        now = q.popleft()
        result.append(now)
        # 해당원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상정렬을 수행한 결과 출력
    print(*result)
topology_sort()