a, b = map(int, input().split())

cnt = 0
flag = False
while True:
    if b == a:
        break
    if b == 1:
        flag = True
        break
    if list(str(b))[-1] == '1':
        b = list(str(b))[:len(list(str(b)))-1]
        b = int(''.join(b))
        cnt += 1
    elif b%2 == 0:
        b = int(b/2)
        cnt += 1
    else:
        flag = True
        break
if flag == False:
    print(cnt+1)
else:
    print(-1)
