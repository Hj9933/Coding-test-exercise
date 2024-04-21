from itertools import combinations
n, k = map(int, input().split())
nums = [i for i in range(n)]

print(len(list(combinations(nums, k))))