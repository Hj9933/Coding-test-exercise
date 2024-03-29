import sys
input = sys.stdin.readline
t = int(input())

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

for _ in range(t):
    n, m = map(int, input().split())
    parent = [0]*(n+1)

    # 모든 간선을 담을 리스트와 최종 개수를 담을 변수
    edges = []
    result = 0

    # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
    for i in range(1, n+1):
        parent[i] = i

    # 모든 간선에 대한 정보 입력받기
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))

    for edge in edges:
        a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1
    print(result)

    