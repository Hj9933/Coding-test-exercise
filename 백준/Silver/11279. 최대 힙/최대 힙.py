import sys
input = sys.stdin.readline

import heapq
n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(q) > 0:
            a = heapq.heappop(q)
            print(a[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (-x, x))
