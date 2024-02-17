import sys

lst = list(sys.stdin.readline().strip())
i = 0
while True:
    i += 10
    print(*lst[i-10:i], sep='')
    if i >= len(lst):
        break
 