# 1715. 카드정렬하기
n = int(input())
nums = list(int(input()) for _ in range(n))
import heapq
heapq.heapify(nums)

if n == 1:
    print(0)
else:
    answer = 0
    while len(nums) >= 2:
        tmp = 0
        tmp += heapq.heappop(nums)
        tmp += heapq.heappop(nums)
        heapq.heappush(nums, tmp)
        answer += tmp

    print(answer)
