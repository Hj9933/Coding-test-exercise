t = int(input())
lst = [int(input()) for _ in range(t)]

d = [0]*11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in lst:
    print(d[i])
