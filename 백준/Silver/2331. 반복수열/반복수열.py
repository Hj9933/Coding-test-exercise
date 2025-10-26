# 2331. 반복수열
a, p = map(int,input().split())

lst = [a]

while True:
    tmp = str(lst[-1])
    tmp_s = 0
    for j in tmp:
        tmp_s += int(j)**p
    if tmp_s in lst:
        k = tmp_s
        break
    else: 
        lst.append(tmp_s)
result = lst[:lst.index(k)]
print(len(result))