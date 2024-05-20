for _ in range(3):
    lst = list(map(int, input().split()))
    cnt = lst.count(0)
    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    else:
        print('E')