import sys
input = sys.stdin.readline

# n에 최대한 가까운데 troub에 있는 숫자는 포함되지 않은 숫자를 찾는 게 관건
n = int(input())
m = int(input())
if m != 0:
    troub = set(list(input().split()))

now = 100
n_close = n
if now != n:
    if m == 0:
        min_click = min(len(list(str(n))), abs(now-n))
        print(min_click)
    elif m == 10: # 모든 키가 다 고장났으면 +,- 버튼으로만 이동
        min_click = abs(now-n)
        print(min_click)
    elif not troub & set(str(n)): # 찾아야하는 채널에 고장난 숫자가 포함되어 있지 않다면 n 숫자배열 길이 또는 abs(now-n)
        min_click = min(len(list(str(n))), abs(now-n))
        print(min_click)
    else:
        flag = False # for문 다 돌아도 찾지 못하면 +, - 버튼으로만 이동해야함
        for i in range(1, abs(now-n)+1):
            if not troub & set(str(n-i)) and n-i >= 0: # 교집합이 있으면, 즉 숫자배열에 고장난 숫자가 포함되어 있다면 계속 진행하고 없으면 숫자 저장하고 반복문 종료; n-i와 n+i가 둘다 되는경우라면 자릿수가 더 작아야하므로 n-i부터 실행
                n_close -= i
                flag = True
                break

            if not troub & set(str(n+i)):
                n_close += i
                flag = True
                break
        if flag == True: # for문을 통해 숫자를 찾았다면
            min_click = min(len(list(str(n_close)))+abs(n-n_close), abs(now-n))
            print(min_click)
        else: # 못찾았다면 +,-로 이동
            min_click = abs(now-n)
            print(min_click)
else:
    print(0)