a = list(input())

if len(a) % 2 == 0:
    b = a[0:len(a)//2]
    c = a[len(a)//2 : len(a)+1]
else:
    b = a[0:int(((len(a))+1)/2) - 1]
    c = a[int(((len(a))+1) / 2 - 1) + 1:]
    
c.reverse()

if b == c:
    print(1)
else:
    print(0)