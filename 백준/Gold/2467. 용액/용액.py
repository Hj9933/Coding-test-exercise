# 2467. 용액
n = int(input())
liq = list(map(int, input().split()))
liq.sort()
s, l = 0, 0
e, r = n-1, n-1

sum_two = liq[l] + liq[r]
while s < e:
    tmp = liq[s] + liq[e]
    if tmp == 0:
        l = s
        r = e
        break
    elif abs(tmp) <= abs(sum_two):
        l = s
        r = e
        if tmp > 0:
            e -= 1
        else:
            s += 1
    elif tmp > 0 and abs(tmp) > abs(sum_two):
        e -= 1
    elif tmp < 0 and abs(tmp) > abs(sum_two):
        s += 1
    sum_two = liq[l] + liq[r]

print(liq[l], liq[r], end=' ')