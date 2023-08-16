lst = list(map(int, input().split()))

lst1 = lst[0:2]
for i in range(2):
    lst1.append(lst[i+2]-lst[i])
    
print(min(lst1))

