import sys
input =sys.stdin.readline

# 1253 좋다
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0
def good(m):
    if m == 0:
        s = 1
    else:
        s = 0
    if m == n-1:
        e = n-2
    else:
        e = n-1

    flag = False
    while s < e:
        tmp = nums[s] + nums[e]
        if tmp == nums[m]:
            flag = True
            break
        elif tmp < nums[m]:
            s += 1
            if s == m:
                s += 1
        else:
            e -= 1
            if e == m:
                e -= 1
    return flag

if n <= 2:
    print(0)
else:
    for i in range(n):
        if good(i):
            result += 1
    print(result)
