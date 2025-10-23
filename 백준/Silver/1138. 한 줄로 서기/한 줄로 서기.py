n = int(input())
taller = list(map(int, input().split()))
lst = [0]*n
k = 1
for i in range(n):
    cnt = taller[i]
    tmp = 0
    for j in range(n):
        if tmp == cnt and lst[j] == 0:
            lst[j] = i+1
            break
        if lst[j] == 0:
            tmp += 1

print(*lst)