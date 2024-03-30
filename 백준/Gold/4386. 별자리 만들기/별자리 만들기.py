import sys
input = sys.stdin.readline
# 최소신장트리
import math
from itertools import combinations

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

# 입력되는 순서대로 0,1,2,3, .. 인덱싱
loc = []
for _ in range(n):
    x, y = map(float, input().split())
    loc.append((x, y))


id = [i for i in range(n)]
edges = []
for comb in combinations(id, 2):
    a, b = comb
    dist = math.dist(loc[a], loc[b])
    edges.append((dist, a, b))


parent = [0]*1001
result = 0

for i in range(n): # 자기자신을 parent로 초기화
    parent[i] = i

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += round(cost, 2)
print(result)