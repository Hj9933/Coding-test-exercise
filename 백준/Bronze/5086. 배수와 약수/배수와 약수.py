T = []
a = 1
b = 1
while a != 0  or b != 0:
    a, b = map(int, input().split())
    T.append([a, b])

for i in range(len(T)-1):
    if T[i][0] == 0 or T[i][1] == 0:
        print('neither')
    elif T[i][0] % T[i][1] == 0:
        print('multiple')
    elif T[i][1] % T[i][0] == 0:
        print('factor')
    else:
        print('neither')