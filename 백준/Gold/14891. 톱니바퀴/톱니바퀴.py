from collections import deque
wheel = list(deque(list(input())) for _ in range(4))

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    tmp = [True]*3
    # 맞물린 톱니바퀴의 극이 다르다면 False로 저장
    if wheel[0][2] != wheel[1][6]:
        tmp[0] = False
    if wheel[1][2] != wheel[2][6]:
        tmp[1] = False       
    if wheel[2][2] != wheel[3][6]:
        tmp[2] = False

    # 기준톱니바퀴 돌리기
    if d == 1:
        wheel[n-1].appendleft(wheel[n-1].pop())
    else:
        wheel[n-1].append(wheel[n-1].popleft())
    
    # 맞물린 톱니바퀴의 극이 다르다면 반대방향으로 돌리기
    i, j = n-2, n-1
    i_d, j_d = -d, -d
    while True:
        if i < 0 or i > 2:
            break
        if tmp[i] == False:
            if i_d == 1:
                wheel[i].appendleft(wheel[i].pop()) 
            else:
                wheel[i].append(wheel[i].popleft()) 
        else:
            break
        i -= 1
        i_d = -i_d
    while True:
        if j < 0 or j > 2:
            break
        if tmp[j] == False:
            if j_d == 1:
                wheel[j+1].appendleft(wheel[j+1].pop()) 
            else:
                wheel[j+1].append(wheel[j+1].popleft()) 
        else:
            break
        j += 1
        j_d = -j_d

S =  [1,2,4,8]

ans = 0
for i in range(4):
    if wheel[i][0] == '1':
        ans += S[i]

print(ans)
