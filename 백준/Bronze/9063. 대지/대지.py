n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
x = []
y = []
for i in range(n):
    x.append(lst[i][0])
    y.append(lst[i][1])
if len(set(x)) >=2 and len(set(y)) >= 2:
    print((max(x)-min(x))*(max(y)-min(y)))
else:
    print(0)