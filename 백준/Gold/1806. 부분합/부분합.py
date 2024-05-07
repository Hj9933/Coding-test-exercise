# 투포인터 문제
from collections import deque
n, s = map(int, input().split())
nums = deque(list(map(int, input().split())))
temp = deque([])

min_len = 100001 # 최소 길이 초기화
accum_sum = 0
count = 0
while nums:
    flag = False
    while True:
        a = nums.popleft()
        temp.append(a)
        accum_sum += a
        count += 1
        if accum_sum >= s:
            flag = True
            break
        if len(nums) == 0:
                break

    
    if flag == True:
        flag_1 = False 
        while accum_sum >= s and len(temp) > 0:
            a = temp.popleft()
            accum_sum -= a
            count -= 1

        count += 1
        temp.appendleft(a)
        accum_sum += a
        min_len = min(min_len, count)


if flag == True:
    print(min_len)
else:
    print(0)