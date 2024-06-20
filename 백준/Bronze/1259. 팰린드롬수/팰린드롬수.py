while True:
    l = list(input())
    if l[0] == '0':
        break
    a = l
    b = list(reversed(l))
    if a == b:
        print("yes")
    else:
        print("no")