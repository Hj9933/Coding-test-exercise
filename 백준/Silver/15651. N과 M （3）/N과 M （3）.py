n, m = map(int, input().split())
lst = [i for i in range(1,n+1)]
from itertools import product
perm_lst = product(lst, repeat = m)

for perm in perm_lst:
    print(*perm)