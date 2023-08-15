lst = [list(map(int, input().split())) for _ in range(3)]

x = []
y = []

for i in range(3):
    x.append(lst[i][0])
    y.append(lst[i][1])

unique_x = list(set(x))
unique_y = list(set(y))

count_x = 0
count_y = 0
for i in range(2):
    if x.count(unique_x[i]) == 1:
        print(unique_x[i], end = ' ')
for i in range(2):
    if y.count(unique_y[i]) == 1:
        print(unique_y[i], end = ' ')