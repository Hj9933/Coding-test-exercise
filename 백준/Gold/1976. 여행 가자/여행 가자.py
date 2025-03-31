import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
## 유니온 파인드
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    roota = find(a)
    rootb = find(b)
    if roota != rootb:
        parent[rootb] = roota

parent = [i for i in range(n)]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            union(i,j)
plan = list(map(int, input().split()))
root = find(plan[0]-1)

flag = True
for city in plan:
    if find(city-1) != root:
        print("NO")
        flag = False
        break
if flag:
    print("YES")
