lst = list(map(int, input().split()))
l = list(range(1, 9))
r = list(range(8, 0, -1))
if lst == l:
    print('ascending')
elif lst == r:
    print('descending')
else:
    print('mixed')