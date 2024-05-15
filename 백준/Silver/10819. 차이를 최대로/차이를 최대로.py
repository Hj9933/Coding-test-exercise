n = int(input())
nums = list(map(int, input().split()))
from itertools import permutations
max_num = -1000
for perm in permutations(nums, n):
    num = 0
    for i in range(n-1):
        num += abs(perm[i] - perm[i+1])
    max_num = max(max_num, num)

print(max_num)