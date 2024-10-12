import sys
input = sys.stdin.readline
# 2110. 공유기설치
n, c = map(int, input().split())
nums = sorted(list(int(input()) for _ in range(n)))
s = 1
e = nums[n-1]-nums[0]
if n == 2:
    print(nums[1]-nums[0])
else:
    while s <= e:
        mid = (s+e)//2
        tmp = nums[0]
        cnt = 1

        for i in range(1, n):
            if nums[i] - tmp >= mid:
                cnt += 1
                tmp = nums[i]

        if cnt < c:
            e = mid-1
        elif cnt >= c:
            s = mid+1
            answer = mid
    print(answer)