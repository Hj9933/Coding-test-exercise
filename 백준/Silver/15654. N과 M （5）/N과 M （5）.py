n, m = map(int, input().split())
nums = list(map(int, input().split()))

from itertools import permutations
for perm in sorted(permutations(nums, m)):
    print(*perm)