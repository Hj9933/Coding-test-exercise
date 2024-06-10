import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
from collections import Counter
cnt = Counter(lst)

pointer = k-1
l = Counter(lst[:pointer])
i = 0
flag = False
while True:
    i += 1
    if flag == True:
        if pointer < n-1:
            l[lst[pointer-1]] += 1
            l[lst[pointer]] += 1
        elif pointer < n:
            l[lst[pointer]] += 1
    else:
        if pointer < n:
            l[lst[pointer]] += 1
    # print(l)
    flag = False
    if l[1] > 0 and l[2] == 0:
        l[1] -= 1
        cnt[1] -= 1
        pointer += 1
        if pointer > n-1:
            break
    elif l[1] == 0 and l[2] > 0:
        l[2] -= 1
        cnt[2] -= 1
        pointer += 1
        if pointer > n-1:
            break
    elif l[1] > 0 and l[2] > 0:
        l[1] -= 1
        l[2] -= 1
        cnt[1] -= 1
        cnt[2] -= 1
        pointer += 2
        flag = True
        if pointer > n-1:
            break


print(i+max(cnt.values()))