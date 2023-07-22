a = []
id = []
for i in range(9):
    lst = list(map(int, input().split()))
    a.append(max(lst))
    id.append([i + 1, lst.index(max(lst)) + 1])

for j in range(1):
    print(max(a))
    for i in range(2):
        print(id[a.index(max(a))][i], end = " ") 