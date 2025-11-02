n = int(input())

import heapq
q = []
for i in range(n):
    lst = list(map(int, input().split()))
    if i == 0:
        for k in lst:
            heapq.heappush(q,k)
    else:
        for k in lst:
            if k > q[0]:
                heapq.heappush(q, k)
                heapq.heappop(q)
print(q[0])