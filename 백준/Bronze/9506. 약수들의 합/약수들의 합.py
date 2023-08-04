while (True):
    n = int(input())
    if n == -1:
        break
    lst = []
    for i in range(1,n):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        print(n, '=', ' + '.join(str(s) for s in lst))
    else:
        print(n, 'is NOT perfect.')