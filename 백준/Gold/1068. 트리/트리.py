import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
r_node = int(input())

indegree = [0]*n
for i in range(n):
    if parent[i] != -1:
        indegree[parent[i]] += 1
    else:
        root = i
if r_node == root:
    print(0)
else:
    indegree[parent[r_node]] -= 1
    indegree[r_node] = -2 # -2는 아예 지운다는 의미
    r = r_node
    q = deque([])
    remove_node = []
    for i in range(n):
        if parent[i] == r:
            remove_node.append(i)
            q.append(i)
            indegree[i] = -2
    while q:
        r = q.popleft()
        for i in range(n):
            if parent[i] == r and i not in remove_node:
                remove_node.append(i)
                q.append(i)
                indegree[i] = -2
    print(indegree.count(0))