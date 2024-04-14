import heapq
import sys
input = sys.stdin.readline
n = int(input())
lst = list(int(input()) for _ in range(n))
q = []
for x in lst:
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if len(q) == 0:
            print(0)
        else:
            abs_x, x = heapq.heappop(q)
            print(x)
