# 강의실 배정
import sys
input = sys.stdin.readline
n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))

lst.sort(key=lambda x: (x[0],x[1]))

import heapq
heap = [lst[0][1]]
for i in range(1,n):
    if heap[0] <= lst[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lst[i][1])
print(len(heap))