import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
from collections import Counter
cnt = Counter(lst)

pointer = k
i = 0
one = 0
two = 0
while True:
    i += 1
    l = Counter(lst[:pointer])
    l[1] -= one
    l[2] -= two
    if l[1] > 0 and l[2] == 0:
        cnt[1] -= 1
        one += 1
        pointer += 1
        if pointer > n:
            pointer = n
    elif l[1] == 0 and l[2] > 0:
        cnt[2] -= 1
        two += 1
        pointer += 1
        if pointer > n:
            pointer = n
    elif l[1] > 0 and l[2] > 0:
        cnt[1] -= 1
        cnt[2] -= 1
        one += 1
        two += 1
        pointer += 2
        if pointer > n:
            pointer = n

    if sum(cnt.values()) == 0:
        break

print(i)