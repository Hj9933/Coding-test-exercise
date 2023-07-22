lst = [list(input()) for _ in range(5)]
a = []
for i in range(5):
    a.append(len(lst[i]))
for i in range(max(a)):
    for j in range(5):
        if len(lst[j]) < i + 1: pass
        else:
            print(lst[j][i], end = '')