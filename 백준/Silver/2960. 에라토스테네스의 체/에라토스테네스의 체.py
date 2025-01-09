n, k = map(int, input().split())
lst = [i for i in range(2, n+1)]
p = []
i=0
ans = 0
while ans != k:
    i  = min(lst)
    p.append(i)
    j = 0
    while True:
        if lst[j] % i == 0:
            ans_n = lst[j]
            del lst[j]
            ans += 1
            if ans == k:
                break
        j += 1
        if j >= len(lst):
            break
print(ans_n)