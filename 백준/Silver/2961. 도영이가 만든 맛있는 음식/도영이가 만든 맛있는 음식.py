import sys
input = sys.stdin.readline

n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))

from itertools import combinations
if n == 1:
    print(abs(lst[0][0] - lst[0][1]))
else:
    min_diff = int(1e9)
    for i in range(1, n+1):
        for j in combinations(lst, i):
            m = 1
            s = 0
            for k in j:
                m = m*k[0]
            for k in j:
                s += k[1]
            min_diff = min(abs(m-s), min_diff)
    print(min_diff)