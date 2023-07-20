a = list(input().upper())
b = list(set(a))

count = []
for i in range(len(b)):
    count.append(a.count(b[i]))

if count.count(max(count)) >= 2:
    print("?")
else:
    print(b[count.index(max(count))])