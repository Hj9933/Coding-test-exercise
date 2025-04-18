# 작업
import sys
input = sys.stdin.readline
n = int(input())
graph = list([] for _ in range(n+1))
dur = [0]*(n+1)
indegree = [0]*(n+1)
for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    dur[i] = tmp[0]
    for j in tmp[2:]:
        graph[j].append(i)
        indegree[i] += 1
from collections import deque
def topology_sort():
    q = deque([])
    result = [0]*(n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        current = q.popleft()
        result[current] += dur[current]
        for i in graph[current]:
            indegree[i] -= 1
            result[i] = max(result[i], result[current])
            if indegree[i] == 0:
                q.append(i)
    return result
result = topology_sort()
print(max(result))
