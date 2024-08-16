import sys
input = sys.stdin.readline
# 1005. ACM Craft - 위상정렬+DP
from collections import deque
def topology_sort():
    result = []
    q = deque()

    # 처음 시작은 진입차수가 0인 노드를 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            distance[i] = time[i-1]

    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            distance[i] = max(distance[i], distance[now] + time[i-1])
            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    distance = [-1]*(n+1)     
    topology_sort()
    print(distance[w])