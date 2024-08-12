import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
truth = list(map(int, input().split()))
result = 0
n_truth = truth[0]
if n_truth != 0:
    truth = truth[1:]
else:
    result = m
    print(result)

parent = [i for i in range(n+1)]
party = []
for _ in range(m):
    party.append(list(map(int, input().split())))

if result == 0:
    for p in party:
        for i in range(1, p[0]):
            union_parent(parent, p[i], p[i+1])
    root_truth = set()
    for t in truth:
        root_t = find_parent(parent, t)
        root_truth.add(root_t)
    for p in party:
        temp = 0
        for i in p[1:]:
            p_i = find_parent(parent, i)
            if p_i not in root_truth:
                temp += 1
        if temp == p[0]:
            result += 1
    print(result)