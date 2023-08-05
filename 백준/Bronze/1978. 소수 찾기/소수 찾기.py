n = int(input())
lst = list(map(int, input().split()))

count = 0
for i in range(n):
    lst1 = []
    for j in range(1, lst[i] + 1):
        if lst[i] % j == 0:
            lst1.append(j)
    if len(lst1) == 2:
        count += 1
print(count)