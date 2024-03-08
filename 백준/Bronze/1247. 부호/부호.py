import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    S = sum(lst)
    if S == 0:
        print(0)
    elif S < 0:
        print('-')
    else:
        print('+')