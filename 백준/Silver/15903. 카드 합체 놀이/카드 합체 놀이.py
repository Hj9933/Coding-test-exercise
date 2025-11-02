n, k = map(int, input().split())
A = list(map(int, input().split()))

import heapq
heapq.heapify(A)

for _ in range(k):
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    heapq.heappush(A,a+b)
    heapq.heappush(A,a+b)
print(sum(A))
