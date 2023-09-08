import sys
input = sys.stdin.readline

t = int(input())
lst = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
    a, b = divmod(lst[i][2], lst[i][0])
    if b == 0:
        b = lst[i][0]
        print(int(str(b)+format(a, '02')))
    else:
        print(int(str(b)+format(a+1, '02')))