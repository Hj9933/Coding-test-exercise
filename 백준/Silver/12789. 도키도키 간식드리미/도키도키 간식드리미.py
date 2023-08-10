import sys 
input = sys.stdin.readline

n = int(input())
curr = list(map(int, input().split()))

lst = []
f = 0
for i in range(1, n+1):
    if f == 1:
        break
    while True:
        if len(curr) > 0 and curr[0] == i:
            curr.pop(0)
            break
        elif len(lst) > 0 and lst[-1] == i:
            lst.pop()
            break
        else:
            if len(lst) > 0 and lst[-1] < curr[0]:
                print('Sad')
                f = 1
                break
            else:
                lst.append(curr[0])
                curr.pop(0)

if len(lst) == 0:
    print('Nice')