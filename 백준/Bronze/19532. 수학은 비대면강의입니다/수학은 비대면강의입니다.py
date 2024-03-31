a, b, c, d, e, f = map(int, input().split())
tmp = b*d-a*e
x = int((b*f-c*e)/tmp)
y = int((c*d-a*f)/tmp)
print(x,y, end = ' ')