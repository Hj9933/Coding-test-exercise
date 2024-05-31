from collections import deque
import sys
input =sys.stdin.readline
t = int(input())

for _ in range(t):
    flag = False
    command = list(input())
    n = int(input())
    if n == 0:
        arr = input()
        arr = []
    else:
        l = input()
        len_l = len(l)
        arr = []
        i = 1
        while True:
            num = ''
            while True:
                if l[i] == ',' or l[i] == ']':
                    i += 1
                    break
                else:
                    num = num + l[i]
                    i += 1
            if len(num) > 0:
                arr.append(int(num))

            if i >= (len_l - 1):
                break
        arr = deque(arr)
    r = 1
    r_cnt = 0
    for i in command:
        if i == 'R':
            r = -r
            r_cnt += 1
        elif i == 'D':
            if len(arr) > 0:
                if r == 1:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                flag = True
                
                print('error')
                break
    if flag == False:
        if r_cnt % 2 == 0:
            answer = list(arr)
        else:
            answer = list(reversed(arr))

        len_ans = len(answer)
        if len_ans == 0:
            print('[]')
        elif len_ans == 1:
            print('[', end='', sep='')
            print(answer[0], end='', sep='')
            print(']', end='', sep='')
            print()
        else:
            for k in range(len_ans):
                if k == 0:
                    print('[', end='', sep='')
                    print(answer[k], end='', sep='')
                    print(',', end='', sep='')
                elif k == len_ans-1:
                    print(answer[k], end='', sep='')
                    print(']', end='', sep='')
                else:
                    print(answer[k], end='', sep='')
                    print(',', end='', sep='')
            print()
                