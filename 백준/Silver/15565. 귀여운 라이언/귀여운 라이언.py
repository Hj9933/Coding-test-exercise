from collections import deque
n, k = map(int, input().split())
nums = deque(list(map(int, input().split())))

q = deque([])
lion_cnt = 0
set_cnt = 0
min_cnt = 10**6
flag = False
while nums:
    num = nums.popleft()
    q.append(num)
    set_cnt += 1
    if num == 1:
        lion_cnt += 1
    if lion_cnt == k:
        min_cnt = min(set_cnt, min_cnt)
        flag = True
        temp = 0
        while temp != 2:
            a = q.popleft()
            set_cnt -= 1
            if a == 1:
                lion_cnt -= 1
                temp += 1
        q.appendleft(a)
        lion_cnt += 1
        set_cnt += 1
if flag == True:      
    print(min_cnt)        
else:
    print(-1)
