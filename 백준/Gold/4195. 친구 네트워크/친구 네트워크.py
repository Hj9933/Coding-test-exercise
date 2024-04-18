import sys
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if x == parent[x]:
        return x
    else:
        p = find_parent(parent, parent[x])
        parent[x] = p
        return parent[x]
 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a
        rel[a] += rel[b]
    print(rel[a])
    
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    f = int(input())
    parent, rel = {}, {}
    for i in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            rel[a] = 1
        if b not in parent:
            parent[b] = b
            rel[b] = 1
        union_parent(parent, a, b)
        