t = int(input())
inp = [input().split() for _ in range(t)]

s = []
for i in range(t):
    s.append(list(inp[i][1]))

r = []
for i in range(t):
    r.append(int(inp[i][0]))

a = []
for i in range(t):
    row = []
    for j in range(len(s[i])):
        row.append(s[i][j]*r[i])
    a.append(row)


for i in range(t):
    print(''.join(a[i]))