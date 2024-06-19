lst = [int(input()) for _ in range(7)]
lst.sort()

cnt = 0
lst1 = []
for num in lst:
    if num%2 != 0:
        lst1.append(num)
        cnt += 1
if cnt == 0:
    print(-1)
else:
    print(sum(lst1))
    print((lst1[0]))
