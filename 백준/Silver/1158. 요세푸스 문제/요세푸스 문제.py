n, k = map(int, input().split())
lst = [i for i in range(1,n+1)]
result = []
i = -1
rem_n = n
while True:
    i += k
    if i > len(lst)-1:
        i = i%len(lst)
    result.append(lst[i])
    del lst[i]
    i -= 1
    rem_n -= 1
    if rem_n == 0:
        break

print('<', end='')
for i in range(n):
    if i == n-1:
        print(result[i], '>',sep='',end='')
    else:
        print(result[i],', ',sep='',end='')  
