import sys
input = sys.stdin.readline
# 2470. 두 용액
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
s,e = 0,n-1
small, large = 0,n-1
limit = abs(nums[small] + nums[large])
while s < e:
    tmp = nums[s] + nums[e]
    if abs(tmp) < limit:
        limit = abs(tmp)
        small = s
        large = e
        if limit == 0:
            break
    if tmp >= 0:
        e -= 1
    else:
        s += 1
print(nums[small], nums[large], end = ' ')