a = list(input())
count = 0
while len(a) > 0:
    if len(a) == 1:
        count += 1
        del a[0]
    elif len(a) == 2:
        if a[0] == 'c' and a[1] == '=':
            del a[0:2]
        elif a[0] == 'c' and a[1] == '-':
            del a[0:2]
        elif a[0] == 'd' and a[1] == '-':
            del a[0:2]
        elif a[0] == 'l' and a[1] == 'j':
            del a[0:2]
        elif a[0] == 'n' and a[1] == 'j':
            del a[0:2]
        elif a[0] == 's' and a[1] == '=':
            del a[0:2]
        elif a[0] == 'z' and a[1] == '=':
            del a[0:2]
        else: 
            del a[0]
        count += 1
    else:
        if a[0] == 'c' and a[1] == '=':
            del a[0:2]
        elif a[0] == 'c' and a[1] == '-':
            del a[0:2]
        elif a[0] == 'd' and a[1] == '-':
            del a[0:2]
        elif a[0] == 'l' and a[1] == 'j':
            del a[0:2]
        elif a[0] == 'n' and a[1] == 'j':
            del a[0:2]
        elif a[0] == 's' and a[1] == '=':
            del a[0:2]
        elif a[0] == 'z' and a[1] == '=':
            del a[0:2]
        elif a[0] == 'd' and a[1] == 'z' and a[2] == '=':
            del a[0:3]
        else:
            del a[0]
        count += 1

print(count)