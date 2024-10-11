import sys
input = sys.stdin.readline
# 2343. 기타레슨
n, m = map(int, input().split())
nums = list(map(int, input().split()))

s = max(nums)
e = sum(nums)

while s <= e:
    mid = (s+e)//2
    sum1 = 0
    cnt = 0
    for i in range(n):
        sum1 += nums[i]
        if sum1 > mid:
            cnt += 1
            sum1 = nums[i]

    cnt += 1
    if cnt <= m:
        answer = mid
        e = mid-1

    elif cnt > m:
        s = mid+1


print(answer)