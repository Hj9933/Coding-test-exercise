

n = int(input())

for _ in range(n):
    stc = []
    str = list(input())
    f = 0 # No 여부
    for s in str:
        if s == '(':
            stc.append(s)
        else:
            if len(stc) > 0 :
                stc.pop()
            else:
                f = 1
                break
    if f == 0 and len(stc) == 0:
        print('YES')
    elif f == 0 and len(stc) > 0:
        print('NO')
    else:
        print('NO')