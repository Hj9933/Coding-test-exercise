a, b, c = map(int, input().split())
lst = [a, b, c]

m = max(lst)
del lst[lst.index(m)]
if sum(lst) <= m :
    total = sum(lst) + sum(lst) - 1
else:
    total = sum(lst) + m

print(total)