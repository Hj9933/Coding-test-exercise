lst = list(int(input()) for _ in range(3))

prod = lst[0]*lst[1]*lst[2]

for i in range(0, 10):
    print(list(str(prod)).count(str(i)))